from django import forms
from inventories.models import Inventory


class DrugForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ('name', 'description', 'expiry_date', 'stocked_date', 'quantity', 'price')
