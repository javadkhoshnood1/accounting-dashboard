from django.contrib import admin
from .models import InvoiceShop,ProductItem
# Register your models here.
@admin.register(InvoiceShop)
class InvoiceShopRegister(admin.ModelAdmin):
    list_display = ("user", "name_company","off","keriyeh","price_nahayi")
@admin.register(ProductItem)
class ProductItemRegister(admin.ModelAdmin):
    list_display = ("user","product","tedad","price","price_kol")