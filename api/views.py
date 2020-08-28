from django.shortcuts import render
from api.models import Printer, Check
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.db.models import Q
from .tasks import render_new_check
import django_rq
import json

class Api_Views(APIView):
    parser_classes = [JSONParser]
    def get(self, request):
        api_key = request.GET.get("api_key","!")
        if api_key == "!" or Printer.objects.filter(api_key=api_key).count() == 0:
            return Response({"status":"error","error":"No such printer"})
        else:
            printer = Printer.objects.get(api_key=api_key)
            checks = Check.objects.filter(Q(point_id=printer.point_id)&Q(type=printer.check_type)&Q(status="1"))
            if checks.count() == 0:
                return Response({"status":"no checks"})
            else:
                list_of_links = []
                for c in checks:
                    list_of_links.append(request.build_absolute_uri(c.pdf_file.url))
                    c.printer_id = printer
                    c.status = "2"
                    c.save()
                return Response({"status":"ok","links":list_of_links})
    def post(self,request):
        order_info = request.data
        pid = order_info["point_id"]
        ord_id = order_info["id"]
        if Printer.objects.filter(point_id=pid).count() == 0:
            return Response({"status":"error","error":"no printers"})
        elif Check.objects.filter(order_id=ord_id).count() != 0:
            return Response({"status":"error","error":"already exists"})
        else:
            Check(
                order_id = ord_id,
                point_id = pid,
                type = order_info["type"],
                order = order_info,
                status = "0"
            ).save()
        render_new_check.delay(order_info)
        return Response({"status":"ok"})