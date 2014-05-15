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

    # amount = forms.CharField(
    #     max_length=40,
    # )
    # quantity = forms.IntegerField(
    #     max_length=40,
    #
    # )

    class Meta:
        model = Drug
        fields = ('drug', 'description', 'amount', 'quantity', 'expiry_date')


class EditDrugForm(forms.ModelForm):
    pass