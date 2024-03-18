from django.contrib import admin
from electronic_products_shop.models import Manufacturer, Supplier, Product, TradeNetwork


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city')
    list_filter = ('city', 'country')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('title', 'supplier_type', 'country', 'city')
    list_filter = ('city', 'country',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'manufacturer')


@admin.register(TradeNetwork)
class TradeNetworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'manufacturer', 'supplier', 'debt_to_supplier')
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        for item in queryset:
            item.debt = 0
            item.save()
        self.message_user(request, f'Задолженность перед поставщиком у выбранных объектов обнулена.')

    clear_debt.short_description = 'Обнулить задолженность'
