
from django.urls import path
from  Admin import views
app_name='Admin'
urlpatterns = [

 path('Homepage/',views.homepage,name="homepage") ,

 path('District/',views.district,name="district") , 
 path('deldistrict/<int:did>',views.deldistrict,name="deldistrict"),
 path('editdistrict/<int:eid>',views.editdistrict,name="editdistrict"),


 path('AdminRegistration/',views.adminreg,name="adminreg"),


 path('Category/',views.category,name="category"),
 path('delcategory/<int:cid>',views.delcategory,name="delcategory"),
 path('editcategory/<int:eid>',views.editcategory,name="editcategory"),

 
 path('Place/',views.place,name="place"),
 path('delplace/<int:did>',views.delplace,name="delplace"),
 path('editplace/<int:eid>',views.editplace,name="editplace"),

 path('Subcategory/',views.subcategory,name="subcategory"),
 path('delsubcategory/<int:did>',views.delsubcategory,name="delsubcategory"),
 path('editsubcategory/<int:eid>',views.editsubcategory,name="editsubcategory"),


 path('Brand/',views.brand,name="brand"),
 path('delbrand/<int:bid>',views.delbrand,name="delbrand"),
 path('editbrand/<int:eid>',views.editbrand,name="editbrand"),

 
 path('NewShop/',views.newshop,name="newshop"),
 path('VerifyShop/<int:id>/',views.verifyshop,name="verifyshop"),
 path('Unverifyshop/<int:id>/',views.unverifyshop,name="unverifyshop"),
 path('AcceptedShop/',views.acceptedshop,name="acceptedshop"),
 path('RejectedShop/',views.rejectedshop,name="rejectedshop"),

path('ViewComplaints/',views.ViewComplaints,name="ViewComplaints"),

path('reply/<int:id>/',views.reply,name="reply"),

path('RepliedComplaints/',views.RepliedComplaints,name="RepliedComplaints"),
path('admindetails/',views.admindetails,name="admindetails"),
path('logout/',views.logout,name="logout") ,

]