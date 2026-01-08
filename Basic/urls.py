
from django.urls import path
from Basic import views
urlpatterns = [
   
   path('Add/',views.add,name="add"),
   path('Largesmall/',views.ls,name="ls"),
   path('Register/',views.reg,name="reg")
]
