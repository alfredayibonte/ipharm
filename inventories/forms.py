from django import forms
from inventories.models import Inventory
from pharmacies.models import Pharmacy


class DrugForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(DrugForm, self).__init__(*args, **kwargs)

    description = forms.CharField(
        max_length=300,
        required=True,
    )
    name = forms.CharField(
        required=True,
    )
    expiry_date = forms.DateField(required=False)
    stocked_date = forms.DateField(required=False)
    quantity = forms.IntegerField(required=False)
    price = forms.DecimalField(required=False, max_digits=6, decimal_places=2)

    def clean_name(self):
        name = self.cleaned_data["name"]
        try:
            Inventory._default_manager.get(name=name)
        except Inventory.DoesNotExist:
            return name
        raise forms.ValidationError(
            self.error_messages['drug already exist'],
            code='duplicate_name',
        )

    class Meta:
        model = Inventory
        fields = ('name', 'description', 'expiry_date', 'stocked_date', 'quantity', 'price')

    def save(self, commit=True):
        if commit:
            pharmacy = Pharmacy.objects.get(user=self.request.user)
            inventory =Inventory.objects.create(
                pharmacy=pharmacy, name=self.request.POST['name'],
                description=self.request.POST['description'],
                )
        return inventory

