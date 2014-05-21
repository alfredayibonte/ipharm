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
from pharmacies.forms import MyRegistrationForm, ContactForm
from pharmacies.models import Pharmacy, Client



#My own logout system.
class Logout(View):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return HttpResponseRedirect(reverse('home'))


class Main(generic.View):
    model = Pharmacy
    template_name = 'registration/main.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Main, self).dispatch(*args, **kwargs)


class Chart(generic.ListView):
    template_name = 'registration/chart_dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class Email(generic.ListView):
    model = Client
    template_name = 'registration/email.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Email, self).dispatch(*args, **kwargs)


class Register(View):
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
            return HttpResponseRedirect(reverse('pharmacies:main'))
        return render(request, self.template_name, {'form': form})


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Contact, self).dispatch(*args, **kwargs)


@login_required()
@require_http_methods(["POST"])
def upload(request):
    f = request.FILES['csv_file']
    content = f.read()
    filestream = StringIO.StringIO(content)
    dialect = csv.Sniffer().sniff(content)
    reader = csv.DictReader(filestream.read().splitlines(), dialect=dialect)
    results = [row for row in reader]
    return HttpResponse("thanks ")