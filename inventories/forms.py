from django import forms
from inventories.models import Inventory, Drug, Upload
from ipharmProject.settings import BASE_DIR
from ipharmProject.utils import load_drugs


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug


class UploadDrugForm(forms.ModelForm):
    csv_file = forms.FileField()

    class Meta:
        model = Upload

    def save(self, commit=True):
        upload = super(UploadDrugForm, self).save(commit=False)
        upload.csv_file = self.cleaned_data['csv_file']
        if commit:
            load_drugs(BASE_DIR("/pic_folder/"+str(upload.csv_file)))
        return upload


class InventoryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(InventoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Inventory

    def save(self, commit=True):
        drug = Drug.objects.get(name=self.request.POST['name'])
        price = self.request.POST['price']
        quantity = self.request.POST['quantity']
        expiry_date = self.request.POST['expiry_date']
        stocked_date = self.request.POST['stocked_date']
        pharmacy = self.request.user
        try:
            inventory = Inventory.objects.get(drug=drug, pharmacy=pharmacy)
        except Inventory.DoesNotExist:
            inventory = Inventory.objects.create(drug=drug,
                                                 pharmacy=pharmacy, quantity=quantity,
                                                 price=price, expiry_date=expiry_date,
                                                 stocked_date=stocked_date)
            return inventory


class EditInventoryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.id = kwargs.pop('id', None)
        super(EditInventoryForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inventory = Inventory.objects.get(id=self.id)
        if self.request.POST.get('price'):
            price = self.request.POST.get('price')
            quantity = self.request.POST.get('quantity')
            expiry_date = self.request.POST.get('expiry_date')
            stocked_date = self.request.POST.get('stocked_date')
            inventory.price = price
            inventory.quantity = quantity
            inventory.expiry_date = expiry_date
            inventory.stocked_date = stocked_date
            inventory.save()

