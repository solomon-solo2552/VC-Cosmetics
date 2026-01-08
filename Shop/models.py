from django.db import models
from Guest.models import *
from Admin.models import *
from Shop.models import *
from User.models import *
# Create your models here.
class tbl_product(models.Model):
    product_name=models.CharField(max_length=30)
    product_price=models.FloatField()
    product_photo=models.FileField(upload_to="Assets/File/Product")
    product_details=models.TextField(max_length=100)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE)


  
class tbl_stock(models.Model):
    stock_quantity=models.IntegerField()
    stock_date=models.DateField(auto_now=True)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    