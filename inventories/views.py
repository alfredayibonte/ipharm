from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.views import generic
from inventories.forms import DrugForm, UploadDrugForm
from inventories.models import Drug
from ipharmProject.utils import load_drugs


class UploadFile(View):
    form_class = UploadDrugForm
    initial = {}
    template_name = 'registration/add_drug.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.initial)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            load_drugs(form.cleaned_data['csv_file'])
            self.initial['csv'] = True
            return HttpResponseRedirect(reverse('inventories:add'))
        self.initial['csv_error'] = True
        return HttpResponseRedirect(reverse('inventories:add'))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UploadFile, self).dispatch(*args, **kwargs)


class AddDrug(View):
    form_class = DrugForm
    initial = {}
    template_name = 'registration/add_drug.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.initial)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        self.initial['name'] = self.request.POST['name']
        self.initial['description'] = self.request.POST['description']
        if form.is_valid():
            form.save()
            self.initial['success'] = True
            return HttpResponseRedirect(reverse('inventories:add'))
        self.initial['error'] = True
        return HttpResponseRedirect(reverse('inventories:add'))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddDrug, self).dispatch(*args, **kwargs)


class Inventory(generic.ListView):
    template_name = 'registration/drug_list.html'
    #context_object_name = 'drug'
    model = Drug

    def get_context_data(self, ** kwargs):
        context = super(Inventory, self).get_context_data( ** kwargs)
        context['drug'] = Drug.objects.all()
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Inventory, self).dispatch(*args, **kwargs)


