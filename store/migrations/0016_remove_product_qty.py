# Generated by Django 3.1.1 on 2020-09-13 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_remove_product_prod_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='qty',
        ),
    ]
