from django.db import models
from pharmacies.models import Pharmacy


class Drug(models.Model):
    drug = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    pharmacy = models.ForeignKey(Pharmacy)





