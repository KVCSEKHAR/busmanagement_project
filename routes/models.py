from django.db import models

# Create your models here.


class Route(models.Model):
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    distance = models.FloatField()

    def __str__(self):
        return f"{self.source} - {self.destination}"
