from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product,Category
# Register your models here.
@admin.register(Product)
class ProductRegister(admin.ModelAdmin):
    list_display = ("title","user", "price","price_selling","percent_sod")
@admin.register(Category)
class ProductRegister(admin.ModelAdmin):
    list_display = ("title","created_at")

# @admin.register(AvailableProduct)
# class AvailableProductRegister(admin.ModelAdmin):
#     list_display = ("user","product","mojodi")