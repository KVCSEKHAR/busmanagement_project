from django.db import models
from datetime import datetime

# Create your models here.

class Buses(models.Model):
    bus_no = models.IntegerField(max_length=3) 
    bus_reg_no = models.CharField( max_length=50)
    bus_route = models.CharField( max_length=50)
    bus_driver_name = models.CharField( max_length=50)
    bus_driver_contact = models.CharField( max_length=50)
    bus_incharge_name = models.CharField( max_length=50)
    bus_incharge_contact = models.CharField( max_length=50)
    bus_model = models.CharField( max_length=50)
    bus_sitting_capacity = models.CharField( max_length=50)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.bus_reg_no



