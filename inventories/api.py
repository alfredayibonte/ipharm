from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from inventories.models import Drug, Inventory
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from pharmacies.models import Pharmacy


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class DrugSerializer(serializers.ModelSerializer):
    filter_fields = ('name',)

    class Meta:
        model = Drug


class PharmacySerializer(serializers.ModelSerializer):
    filter_fields = ('inventory',)
    class Meta:
        model = Pharmacy


class InventorySerializer(serializers.ModelSerializer):
    drug = DrugSerializer()
    pharmacy = PharmacySerializer()
    filter_fields = ('drug', 'pharmacy')

    class Meta:
        model = Inventory


class DrugListApiView(ListCreateAPIView):
    model = Drug
    serializer_class = DrugSerializer


class DrugRetrieveUpdateView(RetrieveUpdateAPIView):
    model = Drug
    serializer_class = DrugSerializer


class InventoryApiView(RetrieveUpdateAPIView):
    model = Inventory
    pharmacy = PharmacySerializer()
    serializer_class = InventorySerializer

class PharmacyApiView(RetrieveUpdateAPIView):
    model = Pharmacy
    serializer_class = PharmacySerializer()