# Generated by Django 5.1.4 on 2024-12-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_email', models.CharField(max_length=30)),
                ('user_password', models.CharField(max_length=30)),
                ('user_address', models.CharField(max_length=30)),
                ('user_contact', models.CharField(max_length=30)),
                ('user_district', models.CharField(max_length=30)),
                ('user_photo', models.CharField(max_length=30)),
            ],
        ),
    ]
