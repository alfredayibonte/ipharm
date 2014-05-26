from django.contrib.webdesign.lorem_ipsum import words
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from inventories.models import Inventory, Drug


def search_helper(count, query):
    import itertools
    model_list = Inventory.objects.filter(title__icontains=query, status=1)
    for L in range(1, count + 1):
        for subset in itertools.permutations(words, L):
            count1 = 1
            query1 = subset[0]
            while count1 != len(subset):
                query1 = query1 + " " + subset[count1]
                count1 += 1
            model_list = Inventory.objects.filter(title__icontains=query1, status=1)
    return (model_list.distinct())




def get_drugs(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        drugs = Drug.objects.filter(name__icontains=q)[:20]
        results = []
        for drug in drugs:
            drug_json = {'name': drug.name, 'description': drug.description}
            results.append(drug_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mime_type = 'application/json'
    return HttpResponse(data, mime_type)