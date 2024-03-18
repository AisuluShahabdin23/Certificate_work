from django.db import models
from users.models import NULLABLE


class Manufacturer(models.Model):
    """ Модель представляет производителя(0-завод) """
    title = models.CharField(max_length=200, verbose_name='Производитель', unique=True)
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Supplier(models.Model):
    """ Модель представляет поставщика """
    SUPPLIER_TYPES = [
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    ]

    title = models.CharField(max_length=200, unique=True, verbose_name='Название поставщика')
    email = models.EmailField(max_length=150, unique=True, verbose_name='Электронная почта поставщика', **NULLABLE)
    supplier_type = models.CharField(choices=SUPPLIER_TYPES, verbose_name='Тип поставщика')
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"


class Product(models.Model):
    """ Модель представляет продукты """
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода продукта на рынок')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Производитель')

    def __str__(self):
        return f'{self.title} {self.model}'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class TradeNetwork(models.Model):
    """ Модель представляет торговую сеть """
    title = models.CharField(max_length=150, verbose_name='Наименование торговой сети')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Производитель')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE, related_name='related_supplier')
    receiver = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Получатель', **NULLABLE, related_name='related_receiver')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Задолженность перед поставщиком', **NULLABLE)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title}, {self.product}, {self.manufacturer},  {self.supplier}, {self.receiver}, {self.created_date}'

    class Meta:
        verbose_name = "Торговая сеть"
        verbose_name_plural = "Торговые сети"
