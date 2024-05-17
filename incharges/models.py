from django.db import models

from buses.models import Buses

# Create your models here.

class Incharge(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    bus = models.OneToOneField(Buses, on_delete=models.CASCADE, related_name='incharge')

    def __str__(self):
        return self.name