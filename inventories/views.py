from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.views import generic
from inventories.forms import DrugForm, UploadDrugForm, InventoryForm
from inventories.models import Drug, Inventory
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


class AddInventory(View):
    form_class = InventoryForm
    initial = {}
    template_name = 'registration/add_inventory.html'

    def get(self, request, *args, **kwargs):
        self.initial['drug'] = Drug.objects.all()
        self.initial['inventory'] = Inventory.objects.filter(pharmacy=self.request.user)
        return render(request, self.template_name, self.initial)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request=request)
        if form.is_valid():
            form.save()
            self.initial['success'] = True
            return HttpResponseRedirect(reverse('inventories:inventory_list'))
        self.initial['error'] = True
        return HttpResponseRedirect(reverse('inventories:add'))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddInventory, self).dispatch(*args, **kwargs)


class DrugList(generic.ListView):
    template_name = 'registration/add_inventory.html'
    model = Drug

    def get_context_data(self, ** kwargs):
        context = super(DrugList, self).get_context_data( ** kwargs)
        context['drug'] = Drug.objects.all()
        context['inventory'] = Inventory.objects.filter(pharmacy=self.request.user)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DrugList, self).dispatch(*args, **kwargs)


class InventoryList(generic.ListView):
    template_name = 'registration/inventory_list.html'
    initial = {}

    def get(self, request, *args, **kwargs):
        self.initial['inventory'] = Inventory.objects.filter(pharmacy=self.request.user)
        return render(request, self.template_name, self.initial)


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InventoryList, self).dispatch(*args, **kwargs)