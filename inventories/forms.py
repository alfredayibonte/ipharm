from django import forms
from inventories.models import Drug


class DrugForm(forms.ModelForm):
    drug = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'drug'})
    )
    description = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'enter message', 'cols': 20, 'rows': 3, 'maxlength': 60})
    )

    amount = forms.CharField(

    )
    quantity = forms.IntegerField(

    )

    class Meta:
        model = Drug
        fields = ('drug', 'description', 'amount', 'quantity', )


class EditDrugForm(forms.ModelForm):
    pass
# drug = models.CharField(max_length=200)
#     description = models.CharField(max_length=200, blank=True)
#     amount = models.IntegerField(blank=True)
#     quantity = models.IntegerField(blank=True)
#     expiry_date = models.DateField(blank=True)
#     pharmacy = models.ForeignKey(Pharmacy)