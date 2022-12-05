from .models import Costumers, Products, Orders
from rest_framework import viewsets, permissions, generics
from .serializers import CostumersSerializers, ProductsSerializers, OrdersSerializers


class CostumersViewSet(viewsets.ModelViewSet):
    queryset = Costumers.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CostumersSerializers


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductsSerializers


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrdersSerializers
