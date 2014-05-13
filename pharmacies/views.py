from django.shortcuts import render
from django.views import generic
from users.models import Customer


class Main(generic.View):
    model = Customer
    template_name = 'registration/main_dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class Chart(generic.ListView):
    template_name = 'registration/chart_dashboard.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Chart(generic.View):
    template_name = 'registration/chart_dashboard.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Email(generic.ListView):
    model = Customer
    template_name = 'registration/base2.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)