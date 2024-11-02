from django.db import models
from jalali_date import datetime2jalali,date2jalali
from accounts.models import User
from product.models import Product
from customer.models import Customer

class ProductItemSale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    price_selling = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="قیمت فروش")
    tedad = models.PositiveBigIntegerField(default=0,verbose_name="موجودی")
    price_kol = models.BigIntegerField(default=0, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name="تاریخ افزودن محصول")

    class Meta:
        verbose_name = "ایتم محصول"
        verbose_name_plural = "ایتم محصولات برای فروش"

    

    def created_date(self):
        return date2jalali(self.created_at)
    

class InvoiceSale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE , null=True,blank=True)
    product = models.ManyToManyField(ProductItemSale,blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name="تاریخ افزودن محصول")
    off = models.IntegerField(default=0, null=True, blank=True, verbose_name="تخفیف  شرکت ")
    price_nahayi = models.BigIntegerField(default=0, null=True, blank=True)
    last_price = models.BigIntegerField(default=0, null=True, blank=True)


    class Meta:
        verbose_name = "فروش  محصول"
        verbose_name_plural = "فروش  محصولات  "

    

    def created_date(self):
        return date2jalali(self.created_at)