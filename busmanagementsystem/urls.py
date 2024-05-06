from django.contrib import admin 
from django.urls import path 
from django.conf.urls.static import static 
from django.conf import  settings 


from .views import index,buses,drivers,routes,incharges,staff,students,addbus 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('buses/', buses, name='buses'),
    path('drivers/', drivers, name='drivers'),
    path('routes/', routes, name='routes'),    
    path('incharges/', incharges, name='incharges'),    
    path('staff/', staff, name='staff'), 
    path('students/', students, name='students'), 
    path('addbus/', addbus, name='addbus'), 

    
]



urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)





