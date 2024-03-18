from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from electronic_products_shop.models import Manufacturer, Supplier, Product, TradeNetwork
from electronic_products_shop.permissions import IsActiveEmployee
from electronic_products_shop.serializers import ManufacturerSerializer, SupplierSerializer, ProductSerializer, \
    TradeNetworkSerializer
import django_filters


class SupplierFilter(django_filters.FilterSet):
    """ Фильтрация объектов по определенной стране """
    class Meta:
        model = Supplier
        fields = ['country']


class SupplierViewSet(viewsets.ModelViewSet):
    """ CRUD для модели поставщика """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter
    permission_classes = [IsActiveEmployee]


class ProductViewSet(viewsets.ModelViewSet):
    """ CRUD для модели Продукты """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]


class TradeNetworkViewSet(viewsets.ModelViewSet):
    """ CRUD для модели Торговой сети """
    queryset = TradeNetwork.objects.all()
    serializer_class = TradeNetworkSerializer
    permission_classes = [IsActiveEmployee]


class ManufacturerAPIView(generics.ListAPIView):
    """ Вывод списка производителей """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsActiveEmployee]


class ManufacturerCreateAPIView(generics.CreateAPIView):
    """ Создание производителя """
    serializer_class = ManufacturerSerializer
    permission_classes = [IsActiveEmployee]


class ManufacturerRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод данных одного производителя """
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = [IsActiveEmployee]


class ManufacturerUpdateAPIView(generics.UpdateAPIView):
    """ Обновление данных производителя """
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = [IsActiveEmployee]


class ManufacturerDestroyAPIView(generics.DestroyAPIView):
    """ Удаление данных производителя """
    queryset = Manufacturer.objects.all()
    permission_classes = [IsActiveEmployee]
