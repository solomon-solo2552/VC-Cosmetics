from django.urls import path
from  Guest import views
app_name='Guest'
urlpatterns = [

path('UserRegistration/',views.userreg,name="userreg") , 
path('ajaxplace/',views.ajaxplace,name="ajaxplace") , 
path('Login/',views.login,name="login") , 
path('ShopRegistration/',views.shopreg,name="shopreg") ,
path('',views.index,name="index") ,
path("forgot-password/", views.forgot_password, name="forgot_password"),
path("reset-password/<str:token>/", views.reset_password, name="reset_password"),
]