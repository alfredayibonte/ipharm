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
    username = serializers.CharField()
    lat = serializers.CharField()
    lng = serializers.CharField()
    telephone = serializers.CharField()
    address = serializers.CharField()
    id = serializers.Field()

    class Meta:
        model = Pharmacy
        fields = ('id', 'email', 'name', 'lat', 'lng', 'telephone', 'address', 'username')


class InventorySerializer(serializers.ModelSerializer):
    drug = DrugSerializer
    pharmacy = PharmacySerializer

    class Meta:
        model = Inventory
        fields = ('id', 'drug', 'pharmacy', 'expiry_date', 'stocked_date', 'price', 'quantity', 'details')


class InventoryUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = ('url', 'price', 'expiry_date', 'drug')