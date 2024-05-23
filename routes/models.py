# routes/models.py
from django.db import models

class Route(models.Model):
    route_name = models.CharField(max_length=100)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    route_number = models.CharField(max_length=10, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.route_name
