import json
from django.http import HttpResponse

def json_response(response_dict, status=200):
    response = HttpResponse(json.dumps(response_dict), content_type="application/json", status=status)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response