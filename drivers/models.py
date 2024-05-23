from django.db import models

from buses.models import Buses

from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    license_number = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    bus_assigned = models.OneToOneField('buses.Buses', on_delete=models.SET_NULL, null=True, blank=True, related_name='driver')

    def __str__(self):
        return self.name
