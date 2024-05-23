# routes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.route_list, name='route_list'),
    path('<int:pk>/', views.route_detail, name='route_detail'),
    path('new/', views.route_create, name='route_create'),
    path('<int:pk>/edit/', views.route_update, name='route_update'),
    path('<int:pk>/delete/', views.route_delete, name='route_delete'),
]
