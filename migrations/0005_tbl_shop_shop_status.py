# Generated by Django 5.1.4 on 2025-01-17 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_tbl_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_shop',
            name='shop_status',
            field=models.IntegerField(default=0),
        ),
    ]
