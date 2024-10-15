from django.db import models
from jalali_date import datetime2jalali,date2jalali
from accounts.models import User
from product.models import Product

class ProductItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    price = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="قیمت خرید")
    tedad = models.PositiveBigIntegerField(default=0,verbose_name="موجودی")
    price_kol = models.BigIntegerField(default=0, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name="تاریخ افزودن محصول")

    class Meta:
        verbose_name = "ایتم محصول"
        verbose_name_plural = "ایتم محصولات برای خرید"

    

    def created_date(self):
        return date2jalali(self.created_at)



class InvoiceShop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(ProductItem,blank=True)
    name_company = models.CharField(max_length=255,verbose_name="شرکت خرید")
    phone_company = models.CharField(max_length=255,null=True,blank=True,verbose_name="شماره شرکت ")
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name="تاریخ افزودن محصول")
    off = models.IntegerField(default=0, null=True, blank=True, verbose_name="تخفیف  شرکت ")
    keriyeh = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="تخفیف  شرکت ")
    price_nahayi = models.BigIntegerField(default=0, null=True, blank=True)
    last_price = models.BigIntegerField(default=0, null=True, blank=True)


    class Meta:
        verbose_name = "خرید  محصول"
        verbose_name_plural = "خرید  محصولات  "

    

    def created_date(self):
        return date2jalali(self.created_at)
    

