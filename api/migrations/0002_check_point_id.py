# Generated by Django 3.0.8 on 2020-07-20 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='point_id',
            field=models.IntegerField(null=True, verbose_name='Номер точки'),
        ),
    ]
