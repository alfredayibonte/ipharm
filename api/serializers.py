from rest_framework import serializers
from inventories.models import Drug, Inventory
from pharmacies.models import Pharmacy


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