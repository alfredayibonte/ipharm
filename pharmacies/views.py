from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.base import View
from pharmacies.forms import MyRegistrationForm
from pharmacies.models import Pharmacy


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



@login_required
class Email(generic.ListView):
    model = Pharmacy
    template_name = 'registration/base2.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


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
