import json
from django.http import HttpResponse
import csv
from inventories.models import Inventory, Drug


def json_response(response_dict, status=200):
    response = HttpResponse(json.dumps(response_dict), content_type="application/json", status=status)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response


def load_drugs(file_path):
    """
    :param file_path
    """
    reader = csv.reader(file_path)
    for row in reader:
        try:
            Drug.objects.get(name__iexact=row[0])
        except Drug.DoesNotExist:
            Drug.objects.get_or_create(name=row[0], description=row[1])
            continue