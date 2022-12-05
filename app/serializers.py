from rest_framework import serializers

from .models import Products, Orders, Costumers


class CostumersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Costumers
        fields = '__all__'


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class OrdersSerializers(serializers.ModelSerializer):
    products = ProductsSerializers(many=True)
    costumer = CostumersSerializers(many=True)

    class Meta:
        model = Orders
        fields = '__all__'

