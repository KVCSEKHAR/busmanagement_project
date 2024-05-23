from django.urls import path 

from .  import views



urlpatterns = [
     path('bus/<int:bus_no>/', views.bus_details, name='bus_details'),
     
    path('', views.bus_list, name='bus_list'),
    path('<int:pk>/', views.bus_details, name='bus_detail'),
    path('create/', views.bus_create, name='bus_create'),
    path('<int:pk>/update/', views.bus_update, name='bus_update'),
    path('<int:pk>/delete/', views.bus_delete, name='bus_delete'),

     
]
