from rest_framework import serializers
from inventories.models import Drug, Inventory
from pharmacies.models import Pharmacy


class DrugSerializer(serializers.ModelSerializer):
    filter_fields = ('name',)

    class Meta:
        model = Drug


class PharmacySerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    lat = serializers.CharField()
    lng = serializers.CharField()

    class Meta:
        model = Pharmacy


class InventorySerializer(serializers.ModelSerializer):
    drug = DrugSerializer
    pharmacy = PharmacySerializer

    class Meta:
        model = Inventory
        fields = ('id', 'drug', 'pharmacy', 'expiry_date', 'stocked_date', 'price', 'quantity', 'details')

