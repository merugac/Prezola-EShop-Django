# Generated by Django 3.1.1 on 2020-09-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20200913_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=0),
        ),
    ]
