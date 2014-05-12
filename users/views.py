from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from users.forms import MyRegistrationForm


class Index(TemplateView):
    template_name = 'index.html'


class Register(View):
    form_class = MyRegistrationForm
    initial = {}
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
<<<<<<< HEAD
=======
        print form.errors
>>>>>>> ec65e5038f38012b5edd77711d18ca082d3a7d42
        if form.is_valid():
            form.save()
            user = auth.authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            auth.login(request, user)
<<<<<<< HEAD
            return HttpResponseRedirect(reverse('index'))
=======
            return HttpResponseRedirect(reverse('pharmacies:main'))
>>>>>>> ec65e5038f38012b5edd77711d18ca082d3a7d42
        return render(request, self.template_name, {'form': form})