from django.db import models
from pharmacies.models import Pharmacy


class Inventory(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    expiry_date = models.DateField(blank=True, null=True)
    stocked_date = models.DateField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    pharmacy = models.ForeignKey(Pharmacy)

    def __unicode__(self):
        return self.name