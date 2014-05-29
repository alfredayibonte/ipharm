import csv
import StringIO
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.http import require_http_methods
from django.views.generic.base import View
from inventories.models import Inventory
from pharmacies.forms import MyRegistrationForm, ContactForm, EditProfileForm
from pharmacies.models import Pharmacy, Client


#My own logout system.
class Logout(View):
    """
    logout for pharmacies
    """

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return HttpResponseRedirect(reverse('home'))


class Main(generic.View):
    """The main dashboard once a pharmacy is logged in """
    model = Pharmacy
    template_name = 'registration/main.html'

    def get(self, request, *args, **kwargs):
        context = {'client': Client.objects.filter(pharmacy=self.request.user),
                   'inventory': Inventory.objects.filter(pharmacy=self.request.user)}
        return render(request, self.template_name)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Main, self).dispatch(*args, **kwargs)


class Chart(generic.ListView):
    template_name = 'registration/chart_dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SMS(generic.ListView):
    model = Client
    template_name = 'registration/sms.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SMS, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SMS, self).get_context_data(**kwargs)
        pharmacy = Pharmacy.objects.get(user=self.request.user)
        context['client'] = Client.objects.filter(pharmacy=pharmacy)
        return context


class Email(generic.ListView):
    model = Client
    template_name = 'registration/email.html'

    def get_context_data(self, **kwargs):
        context = super(Email, self).get_context_data(**kwargs)
        context['client'] = Client.objects.filter(pharmacy=self.request.user)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Email, self).dispatch(*args, **kwargs)


class EditProfile(View):
    model = Pharmacy
    form_class = EditProfileForm
    initial = {}
    template_name = 'registration/edit_profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditProfile, self).dispatch(*args, **kwargs)


class Register(View):
    """
    class for registering pharmacies
    """
    form_class = MyRegistrationForm
    initial = {}
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            auth.login(request, user)
            return HttpResponseRedirect(reverse('pharmacies:main'))
        return render(request, self.template_name, {'form': form})


class PharmacyProfile(View):
    """
    This class views pharmacy's profile and one can edit his profile in this class.
    """
    model = Pharmacy
    form_class = EditProfileForm
    template_name = 'registration/user.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pharmacies:pharmacy'))
        return HttpResponseRedirect(reverse('pharmacies:pharmacy'))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PharmacyProfile, self).dispatch(*args, **kwargs)


class ContactList(generic.ListView):
    model = Client
    template_name = 'registration/client_list.html'

    def get_context_data(self, **kwargs):
        context = super(ContactList, self).get_context_data(**kwargs)
        context['client'] = Client.objects.filter(pharmacy=self.request.user)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactList, self).dispatch(*args, **kwargs)


class Contact(View):
    model = Client
    initial = {}
    form_class = ContactForm
    template_name = 'registration/contact.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request=request)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pharmacies:contact_list'))
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Contact, self).dispatch(*args, **kwargs)


class MAP(generic.ListView):
    template_name = 'registration/map.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MAP, self).dispatch(*args, **kwargs)



