from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from api.serializers import DrugSerializer, InventorySerializer, PharmacySerializer
from inventories.models import Drug, Inventory
from pharmacies.models import Pharmacy

from rest_framework import viewsets


class DrugListApiView(ListCreateAPIView):
    model = Drug
    serializer_class = DrugSerializer


class DrugRetrieveUpdateView(RetrieveUpdateAPIView):
    model = Drug
    serializer_class = DrugSerializer


class PharmacyApiView(viewsets.ModelViewSet):
    model = Pharmacy
    serializer_class = PharmacySerializer


class InventoryApiView(ListCreateAPIView):
    model = Inventory
    serializer_class = InventorySerializer


class GetInventoryApiView(viewsets.ModelViewSet):
    model = Inventory
    serializer_class = InventorySerializer

