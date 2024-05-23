from django.urls import path 

from .  import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('admin/',views.admin,name='admin'),
    path('driver/',views.driver,name='driver'),
    path('incharge/',views.incharge,name='incharge'),
    path('student/',views.student,name='student'),
         
]



