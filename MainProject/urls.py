
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   
   path('Basic/',include('Basic.urls')),
   path('Admin/',include('Admin.urls')),
   path('',include('Guest.urls')),
   path('User/',include('User.urls')),
   path('Shop/',include('Shop.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)