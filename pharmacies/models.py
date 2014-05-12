from django.db import models
from users.models import Customer


class Pharmacy(models.Model):
    name = models.CharField(max_length=100, blank=False)
    contact_number = models.CharField(max_length=14, blank=True)
    lat = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(Customer)


class Contact_list(models.Model):
    pharmacy = models.ForeignKey(Pharmacy)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=100)


