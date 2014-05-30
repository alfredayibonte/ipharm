from django import forms
from inventories.models import Inventory, Drug, Upload
from ipharmProject.settings import BASE_DIR
from ipharmProject.utils import load_drugs
from pharmacies.models import Pharmacy

# class MyRegistrationForm(forms.ModelForm):
#      def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request', None)
#         super(DrugForm, self).__init__(*args, **kwargs)


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


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory