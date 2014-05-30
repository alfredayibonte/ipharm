from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from api.serializers import DrugSerializer, InventorySerializer, PharmacySerializer
from inventories.models import Drug, Inventory
from pharmacies.models import Pharmacy

from rest_framework import viewsets


class DrugApiView(viewsets.ModelViewSet):
    model = Drug
    serializer_class = DrugSerializer


class PharmacyApiView(viewsets.ModelViewSet):
    model = Pharmacy
    serializer_class = PharmacySerializer


class InventoryApiView(viewsets.ModelViewSet):
    model = Inventory
    serializer_class = InventorySerializer

