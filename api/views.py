from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from api.serializers import DrugSerializer, InventorySerializer, PharmacySerializer
from inventories.models import Drug, Inventory
from pharmacies.models import Pharmacy

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
        print 'drug id is '+drug_id
        drug = Drug.objects.get(pk=drug_id)
        inventory = Inventory.objects.filter(drug=drug)
        for i in inventory:
            ls.append(i.pharmacy)
        pharmacies = PharmacySerializer(ls, many=True)

        return Response(pharmacies.data, status=HTTP_200_OK)


# class FindPharmacyView(viewsets.ModelViewSet):
#
#     def list(self, request):
#         queryset = Pharmacy.objects.all()
#         serializer = PharmacySerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         print pk
#         queryset = Drug.objects.all()
#         # user = get_object_or_404(queryset, pk=pk)
#         serializer = DrugSerializer(user)
#         return Response(serializer.data)