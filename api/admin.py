from django.contrib import admin
from api.models import Check, Printer

# Register your models here.
class PrinterAdmin(admin.ModelAdmin):
    list_display=("name","check_type","point_id")

class CheckAdmin(admin.ModelAdmin):
    list_display=("printer_id","order_id","type","status")

admin.site.register(Printer, PrinterAdmin)
admin.site.register(Check, CheckAdmin)