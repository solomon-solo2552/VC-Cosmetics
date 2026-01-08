from django.db import models
from Shop.models import tbl_product
from User.models import *
from Guest.models import *
from Admin.models import *
from Shop.models import *
# Create your models here.



class tbl_feedback(models.Model):
    feedback_date=models.DateField()
    feedback_content=models.TextField(max_length=100)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    booking_amount = models.CharField(max_length=30)
    booking_status = models.IntegerField(default=0)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_cart(models.Model):
    cart_qty = models.IntegerField(default=1)
    cart_status = models.IntegerField(default=0)
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    booking = models.ForeignKey(tbl_booking, on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.IntegerField(default=0)
    complaint_content=models.TextField(max_length=100)
    complaint_reply=models.TextField(max_length=100)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    product=models.ForeignKey(tbl_product, on_delete=models.CASCADE)


class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)