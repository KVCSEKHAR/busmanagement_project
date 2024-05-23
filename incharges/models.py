# incharges/models.py

from django.db import models

class Incharge(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    assigned_bus = models.OneToOneField('buses.Buses', on_delete=models.SET_NULL, null=True, blank=True, related_name='incharge')

    def __str__(self):
        return self.name
