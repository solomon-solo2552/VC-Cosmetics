from django.urls import path
from Shop import views
app_name='Shop'
urlpatterns = [
    path('ajaxcategory/',views.ajaxcategory,name="ajaxcategory"),
    path('Product/',views.product,name="product"),
    path('delproduct/<int:pid>',views.delproduct,name="delproduct"),
    path('addstock/<int:pid>',views.addstock,name="addstock"),

    path('Homepage/',views.homepage,name="homepage") ,
    path('Myprofile/',views.myprofile,name="myprofile") ,
    path('Editprofile/',views.editprofile,name="editprofile") , 
    path('ChangePassword/',views.changepassword,name="changepassword") , 

    path('ViewBooking/',views.viewbooking,name="viewbooking") , 
    path('packed/<int:bid>',views.packed,name="packed") , 
    path('shipped/<int:sid>',views.shipped,name="shipped") , 
    path('delivered/<int:did>',views.delivered,name="delivered") ,
    path('complete/<int:cid>',views.complete,name="complete") ,

    path('logout/',views.logout,name="logout") ,




]