from django.db import models


class Pharmacy(models.Model):
    name = models.CharField(max_length=100, blank=False)
    contact_number = models.IntegerField(max_length=14)
    lat = models.IntegerField()
    long = models.IntegerField()
    location_name = models.CharField(max_length=200)

