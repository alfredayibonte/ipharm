from django.contrib.auth.models import User, Group
from rest_framework import serializers
from inventories.models import Drug
from pharmacies.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ('url', 'name', 'description')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



#views
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Drug.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Drug.objects.all()
    serializer_class = GroupSerializer


class DrugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drug