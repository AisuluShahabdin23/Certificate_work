from rest_framework import serializers
from electronic_products_shop.models import TradeNetwork, Product, Manufacturer, Supplier


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class TradeNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeNetwork
        fields = '__all__'
        read_only_fields = ('debt_to_supplier',)
