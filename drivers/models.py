from django.db import models

# Create your models here.



class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20, unique=True)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name