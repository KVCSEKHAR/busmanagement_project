from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20, unique=True)
    # Other student-related fields

    def __str__(self):
        return self.name
