from django.db import models

from buses.models import Buses
# Create your models here.



# class Driver(models.Model):
#     name = models.CharField(max_length=100)
#     license_number = models.CharField(max_length=20, unique=True)
#     contact_number = models.CharField(max_length=15)

#     def __str__(self):
#         return self.name


class Driver(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    bus = models.OneToOneField(Buses, on_delete=models.CASCADE, related_name='driver')

    def __str__(self):
        return self.name