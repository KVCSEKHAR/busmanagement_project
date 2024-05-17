from django.db import models

# Create your models here.

from buses.models import Buses


class Route(models.Model):
    name = models.CharField(max_length=50)
    buses = models.ManyToManyField(Buses, related_name='routes')

    def __str__(self):
        return self.name
