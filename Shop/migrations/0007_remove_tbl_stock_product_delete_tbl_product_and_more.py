# Generated by Django 5.1.6 on 2025-02-17 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_remove_tbl_product_brand'),
        ('User', '0007_remove_tbl_complaint_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_stock',
            name='product',
        ),
        migrations.DeleteModel(
            name='tbl_product',
        ),
        migrations.DeleteModel(
            name='tbl_stock',
        ),
    ]
