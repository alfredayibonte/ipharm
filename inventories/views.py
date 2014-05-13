from django.shortcuts import render, render_to_response

# Create your views here.
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from inventories.models import Drug
from ipharmProject.utils import json_response


class DrugSearch(generic.ListView):
    model = Drug
    template_name = 'registration/base2.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

@require_http_methods(["POST"])
def search(request):
    drugs = []
    if request.POST and request.POST['search'] != '':
        search_text = request.POST['search']
        drugs = Drug.objects.filter(name__icontains=search_text)
        return render_to_response('search.html', {'drugs': drugs})
    elif request.POST and request.POST['search_text'] == '':
        return render_to_response('search.html', {'drugs': drugs})
    return render_to_response('search.html', {'drugs': drugs})

