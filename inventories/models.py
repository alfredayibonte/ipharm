from django.db import models
from pharmacies.models import Pharmacy



class Drug(models.Model):
    drug = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    amount = models.IntegerField(blank=True)
    quantity = models.IntegerField(blank=True)
    expiry_date = models.DateField(blank=True)
    pharmacy = models.ForeignKey(Pharmacy)





