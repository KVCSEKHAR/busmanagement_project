from django.db import models

from buses.models import Buses
# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=50)
    boarding_point = models.CharField(max_length=50)
    bus = models.ForeignKey(Buses, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.roll_number})"
