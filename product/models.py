from django.db import models

# Create your models here.
from django.db import models
from jalali_date import datetime2jalali,date2jalali
from accounts.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name="اسم سته بندی")
    discription = models.TextField(max_length=300, null=True, blank=True, verbose_name="توضیحات مدیر")
    created_at = models.DateTimeField(null=True, auto_now_add=True, blank=True, verbose_name="تاریخ اضافه شدن ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها "

    def created_date(self):
        return date2jalali(self.created_at)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=True, blank=True, verbose_name="نام محصول")
    image = models.ImageField(upload_to="productimage", null=True, blank=True, verbose_name="عکس محصول")
    price = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="قیمت خرید")
    price_selling = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="قیمت فروش")
    percent_sod = models.IntegerField(default=0, null=True, blank=True)
    is_mojod = models.BooleanField(default=False)
    mojodi = models.BigIntegerField(default=0)
    sod = models.BigIntegerField(default=0)
    discription = models.TextField(max_length=300, null=True, blank=True, verbose_name="توضیحات مدیر")
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name="تاریخ افزودن محصول")
    category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE, verbose_name="دسته بندی ها ")


    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ["-id"]    
    def sod_khles(self):
        self.sod = self.price_selling - self.price
        self.save()
        return self.sod
        

    def __str__(self):
        return self.title

    def created_date(self):
        return date2jalali(self.created_at)



# class AvailableProduct(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     mojodi = models.PositiveBigIntegerField(default=0,verbose_name="موجودی")
#     company = models.CharField(max_length=255,verbose_name="شرکت خرید")
#     status = models.BooleanField(default=True)
#     discription = models.TextField(max_length=300, null=True, blank=True, verbose_name="توضیحات مدیر")
#     created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name="تاریخ افزودن محصول")
#     price = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="قیمت خرید")
#     price_kol = models.BigIntegerField(default=0, null=True, blank=True)
#     off = models.IntegerField(default=0, null=True, blank=True, verbose_name="تخفیف  شرکت ")


#     class Meta:
#         verbose_name = "خرید  محصول"
#         verbose_name_plural = "خرید  محصولات  "

    

#     def Created_at(self):
#         return date2jalali(self.created_at)