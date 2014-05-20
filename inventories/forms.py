from django import forms
from inventories.models import Inventory
from pharmacies.models import Pharmacy


class DrugForm(forms.Form):
    description = forms.CharField(
        max_length=300,
        required=False,
    )
    expiry_date = forms.DateField(required=False)
    stocked_date = forms.DateField(required=False)
    quantity = forms.IntegerField(required=False)
    price = forms.DecimalField(required=False, max_digits=6, decimal_places=2)

    class Meta:
        model = Inventory
        fields = ('name', 'description', 'expiry_date', 'stocked_date', 'quantity', 'price')
