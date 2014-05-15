from django import forms
from inventories.models import Drug


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ('drug', 'description', 'amount', 'quantity', 'expiry_date')





class EditDrugForm(forms.ModelForm):
    pass
