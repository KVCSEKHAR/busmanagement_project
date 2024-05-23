# students/models.py
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    student_id = models.CharField(max_length=10, unique=True)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
