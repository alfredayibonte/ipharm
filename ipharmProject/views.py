<<<<<<< HEAD
from django.views.generic.base import View


class Home(View):
=======
from django.shortcuts import render
from django.views.generic.base import View, TemplateView


class Home(TemplateView):
>>>>>>> ec65e5038f38012b5edd77711d18ca082d3a7d42
    template_name = 'index.html'