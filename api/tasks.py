import os
from api.models import Check
from django_rq import job
@job
def render_new_check(info):
    order_id = info["id"]
    products = info["products"]
    type = "kitchen" if info['type'] == "0" else "client"
    tmp_name = f"media/pdf/tmp_{order_id}.html"
    with open(tmp_name,"w") as f:
        f.write(f'<html><meta http-equiv="content-type" content="text/html; charset=utf-8" /><h2>Чек № {order_id}</h2><br/><ul>')
        for p in products:
            f.write(f"<li>{p}</li>")
        f.write("</ul></html>")
    os.system(f"wkhtmltopdf {tmp_name} media/pdf/{order_id}_{type}.pdf")
    os.remove(tmp_name)
    order = Check.objects.get(order_id = order_id)
    order.status = "1"
    order.pdf_file = f"pdf/{order_id}_{type}.pdf"
    order.save()
