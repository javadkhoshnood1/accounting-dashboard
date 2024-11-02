from django.contrib import admin
from .models import InvoiceSale,ProductItemSale
# Register your models here.
@admin.register(InvoiceSale)
class InvoiceSaleRegister(admin.ModelAdmin):
    list_display = ("user", "customer","off","price_nahayi","last_price")
@admin.register(ProductItemSale)
class ProductItemSaleRegister(admin.ModelAdmin):
    list_display = ("user","product","tedad","price_selling","price_kol")