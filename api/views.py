from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from api.serializers import DrugSerializer, InventorySerializer, PharmacySerializer
from inventories.models import Drug, Inventory
from pharmacies.models import Pharmacy


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
