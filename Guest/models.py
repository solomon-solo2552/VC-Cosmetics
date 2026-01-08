from django.db import models
from Admin.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_email=models.CharField(max_length=30)
    user_password=models.CharField(max_length=30)
    user_address=models.CharField(max_length=30)
    user_contact=models.CharField(max_length=30)
    user_photo=models.FileField(upload_to="Assets/File/User")
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    
class tbl_shop(models.Model):
    shop_name=models.CharField(max_length=30)
    shop_email=models.CharField(max_length=30)
    shop_password=models.CharField(max_length=30)
    shop_address=models.CharField(max_length=30)
    shop_contact=models.CharField(max_length=30)
    shop_logo=models.FileField(upload_to="Assets/File/Shop")
    shop_proof=models.FileField(upload_to="Assets/File/Shop")
    shop_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)