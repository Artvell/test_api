from django.db import models
from jsonfield import JSONField

# Create your models here.

class Printer(models.Model):
    choices = [
        ("0", "kitchen"),
        ("1", "client")
    ]
    objects=models.Manager()
    name = models.CharField(max_length=50,verbose_name="Название принтера")
    api_key = models.CharField(max_length=50,verbose_name="Ключ доступа к API",unique=True)
    check_type = models.CharField(max_length=1,verbose_name="Тип чека", choices=choices)
    point_id = models.IntegerField(verbose_name="Номер точки")
    
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Принтер"
        verbose_name_plural = "Принтеры"


class Check(models.Model):
    choices = [
        ("0", "kitchen"),
        ("1", "client")
    ]
    status_choices = [
        ("0","new"),
        ("1","rendered"),
        ("2","printed")
    ]
    objects = models.Manager()
    order_id = models.IntegerField(verbose_name="Номер чека", null = True, unique=True)
    printer_id = models.ForeignKey(Printer, on_delete=models.CASCADE, verbose_name="ID принтера", null = True)
    point_id = models.IntegerField(verbose_name="Номер точки", null = True)
    type = models.CharField(max_length=50,verbose_name="Тип чека", choices=choices)
    order = JSONField(verbose_name="Информация о заказе")
    status = models.CharField(verbose_name="Статус чека",max_length=1,choices=status_choices)
    pdf_file = models.FileField(verbose_name="Ссылка на pdf",upload_to="media/pdf",null = True)

    class Meta:
        verbose_name = "Чек"
        verbose_name_plural = "Чеки"

