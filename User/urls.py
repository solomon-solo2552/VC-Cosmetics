from django.urls import path
from  User import views
app_name='User'
urlpatterns = [
path('Homepage/',views.homepage,name="homepage") , 
path('Myprofile/',views.myprofile,name="myprofile") ,
path('Editprofile/',views.editprofile,name="editprofile") , 
path('ChangePassword/',views.changepassword,name="changepassword") , 
path('Complaints/<int:pid>',views.complaints,name="complaint"),
path('delcomplaint/<int:did>',views.delcomplaint,name="delcomplaint"),

path('Feedback/',views.feedback,name="feedback"),
path('ViewProduct/',views.viewproduct,name="viewproduct"),
path('ajaxsearch/',views.ajaxsearch,name="ajaxsearch"),
path('AddCart/<int:id>/',views.Addcart,name="Addcart"),

path('Addcart/<int:pid>',views.Addcart, name='Addcart'),   
path('Mycart/',views.Mycart, name='Mycart'),   
path("DelCart/<int:did>", views.DelCart,name="delcart"),
path("CartQty/", views.CartQty,name="cartqty"),

path("loader/", views.loader,name="loader"),
path('paymentsuc/',views.paymentsuc, name='paymentsuc'),
path("productpayment/", views.productpayment,name="productpayment"),


path('MyBooking/',views.MyBooking,name="MyBooking"),
path("Cancel/<int:cid>", views.cancel,name="cancel"),


path('MyComplaint/',views.MyComplaint,name="MyComplaint"),
path('delcomplaint1/<int:did>',views.delcomplaint1,name="delcomplaint1"),

path('rating/<int:mid>',views.rating,name="rating"),  
path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
path('starrating/',views.starrating,name="starrating"),
path('search/', views.search_products, name='search_products'),
path('ajaxcategory/',views.ajaxcategory,name="ajaxcategory"),

path('logout/',views.logout,name="logout"),
]