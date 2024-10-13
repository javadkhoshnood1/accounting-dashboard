from django.db import models
from jalali_date import datetime2jalali,date2jalali
from accounts.models import User
# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200, null=True, blank=True, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=12, verbose_name="شماره تماس")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده ")
    price = models.BigIntegerField(default=0,verbose_name="حساب در فروشگاه")
    price_paid_all = models.BigIntegerField(default=0,verbose_name=" پول  پرداختی  ای کل    ")
    price_mandeh = models.BigIntegerField(default=0,verbose_name="باقی مانده در فروشگاه")
    discription = models.TextField(max_length=300, null=True, blank=True, verbose_name="توضیحات مدیر")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ  ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ اضافه شدن")

    image = models.ImageField(upload_to="customer/", null=True, blank=True, verbose_name="عکس پروفایل")
    address = models.TextField(null=True,blank=True,verbose_name="ادرس کاربر")


    def created_date(self):
        return date2jalali(self.created_at)
    
    def updated_date(self):
        return date2jalali(self.updated_at)

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتری ها  "
        ordering = ["-id"]    

    def __str__(self):
        return self.phone


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    discription = models.TextField(max_length=300, null=True, blank=True, verbose_name="توضیحات مدیر")
    price_paid = models.BigIntegerField(default=0,verbose_name=" پول  پرداختی لحظه ای   ")
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True, verbose_name="تاریخ اضافه شدن")

    def created_data(self):
        return date2jalali(self.created_at)
    
    class Meta:
        verbose_name = "پرداخت  "
        verbose_name_plural = "لیست پرداخت ها "
