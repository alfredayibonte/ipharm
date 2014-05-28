from django.db import models
from pharmacies.models import Pharmacy


class Drug(models.Model):
    name = models.CharField(max_length=300, unique=True, blank=False)
    description = models.CharField(max_length=1500, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Inventory(models.Model):
    expiry_date = models.DateField(blank=True, null=True)
    stocked_date = models.DateField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    pharmacy = models.ForeignKey(Pharmacy)
    drug = models.ForeignKey(Drug)
    details = models.CharField(blank=True, null=True, max_length=700)

    class Meta:
        unique_together = ('drug', 'pharmacy',)

    def __unicode__(self):
        return self.quantity


class Upload(models.Model):
    csv_file = models.FileField(upload_to='media/', default='no.csv')



