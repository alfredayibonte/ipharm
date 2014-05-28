from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic.base import View
from inventories.forms import DrugForm, UploadDrugForm
from inventories.models import Inventory, Drug
from rest_framework.parsers import JSONParser
from ipharmProject.utils import load_drugs


class DrugSearch(generic.ListView):
    model = Inventory
    template_name = 'registration/base2.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class UploadFile(View):
    form_class = UploadDrugForm
    initial = {}
    template_name = 'registration/add_drug.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            load_drugs(form.cleaned_data['csv_file'])
            return HttpResponseRedirect(reverse('pharmacies:main'))
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UploadFile, self).dispatch(*args, **kwargs)





@require_http_methods(["POST"])
def search(request):
    drugs = []
    if request.POST and request.POST['search'] != '':
        search_text = request.POST['search']
        drugs = Drug.objects.filter(name__icontains=search_text)
        return render_to_response('drugs.html', {'drugs': drugs})
    elif request.POST and request.POST['search_text'] == '':
        return render_to_response('drugs.html', {'drugs': drugs})
    return render_to_response('drugs.html', {'drugs': drugs})


class AddDrug(View):
    form_class = DrugForm
    initial = {}
    template_name = 'registration/add_drug.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request=request)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pharmacies:main'))
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddDrug, self).dispatch(*args, **kwargs)

