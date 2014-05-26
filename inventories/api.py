from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
# ViewSets define the view behavior.
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer, YAMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class UserCountView(APIView):
    """
    A view that returns the count of active users, in JSON or YAML.
    """
    renderer_classes = (JSONRenderer, YAMLRenderer)

    def get(self, request, format=None):
        user_count = User.objects.filter(active=True).count()
        content = {'user_count': user_count}
        return Response(content)