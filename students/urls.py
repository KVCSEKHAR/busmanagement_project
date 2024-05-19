from django.urls import path 

from .  import views



urlpatterns = [
     path('student/<str:roll_number>/', views.student_details, name='student_details'),
    
]
