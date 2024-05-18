from django.urls import path 

from .  import views



urlpatterns = [
     path('bus/<int:bus_no>/', views.bus_details, name='bus_details'),

     
]
