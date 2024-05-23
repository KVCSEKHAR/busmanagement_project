# incharges/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.incharge_list, name='incharge_list'),
    path('<int:pk>/', views.incharge_details, name='incharge_details'),
    path('create/', views.incharge_create, name='incharge_create'),
    path('<int:pk>/edit/', views.incharge_update, name='incharge_update'),
    path('<int:pk>/delete/', views.incharge_delete, name='incharge_delete'),
]
