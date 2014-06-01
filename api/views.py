from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from api.serializers import DrugSerializer, InventorySerializer, PharmacySerializer, InventoryUpdateSerializer
from inventories.models import Drug, Inventory
from pharmacies.models import Pharmacy
from rest_framework import permissions

from rest_framework import viewsets
from rest_framework import views

from rest_framework.status import HTTP_200_OK


class DrugApiView(viewsets.ModelViewSet):
    model = Drug
    serializer_class = DrugSerializer


class PharmacyApiView(viewsets.ModelViewSet):
    model = Pharmacy
    serializer_class = PharmacySerializer


class InventoryApiView(viewsets.ModelViewSet):
    model = Inventory
    serializer_class = InventorySerializer


class FindPharmacyView(views.APIView):
    model = Inventory

    def get(self, request, *args, **kwargs):
        ls = []
        drug_id = request.QUERY_PARAMS.get('id', None)
        drug = Drug.objects.get(pk=drug_id)
        inventory = Inventory.objects.filter(drug=drug)
        for i in inventory:
            ls.append(i.pharmacy)
        pharmacies = PharmacySerializer(ls, many=True)

        return Response(pharmacies.data, status=HTTP_200_OK)


class InventoryUpdateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Inventory.objects.all()
    serializer_class = InventoryUpdateSerializer
    #permission_classes = permissions.IsAdminUser