from django.urls import path 

from .  import views



urlpatterns = [
    path('register/',views.register,name='register'),
    # path('adminlogin/',views.adminlogin,name='login'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
     
]



