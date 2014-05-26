from django import forms
from inventories.models import Inventory, Drug, Upload
from ipharmProject.settings import BASE_DIR
from ipharmProject.utils import load_drugs
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
            Drug._default_manager.get(name=name)
        except Drug.DoesNotExist:
            return name
        raise forms.ValidationError(
            self.error_messages['drug already exist'],
            code='duplicate_name',
        )

    class Meta:
        model = Inventory
        fields = ('expiry_date', 'stocked_date', 'quantity', 'price')

    def save(self, commit=True):
        if commit:
            pharmacy = Pharmacy.objects.get(user=self.request.user)
            old_drug, new_drug = Drug.objects.get_or_create(
                name=self.request.POST['name'],
                description=self.request.POST['description'])
            if new_drug:
                inventory = Inventory.objects.create(drug=new_drug, pharmacy=pharmacy)
        return inventory


class UploadDrugForm(forms.ModelForm):
    csv_file = forms.FileField()

    class Meta:
        model = Upload

    def save(self, commit=True):
        upload = super(UploadDrugForm, self).save(commit=False)
        upload.csv_file = self.cleaned_data['csv_file']
        if commit:
            #upload.save()
            load_drugs(BASE_DIR("/pic_folder/"+str(upload.csv_file)))
        return upload


