from django.views.generic.base import View


class Home(View):
    template_name = 'index.html'