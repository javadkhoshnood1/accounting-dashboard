from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from jalali_date import datetime2jalali,date2jalali


class MyUserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError("Users must have an email address")

        user = self.model(
            phone=self.normalize_email(phone),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    fullname = models.CharField(max_length=200, null=True, blank=True, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=12, unique=True, verbose_name="شماره تماس")
    name_shop = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_admin = models.BooleanField(default=False, verbose_name="ادمین")
    email = models.EmailField(null=True, blank=True, verbose_name="ایمیل")
    discription = models.TextField(max_length=300, null=True, blank=True, verbose_name="توضیحات کاربر")
    created_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ اضافه شدن")
    image = models.ImageField(upload_to="user_image", null=True, blank=True, verbose_name="عکس پروفایل")
    address = models.TextField(null=True,blank=True,verbose_name="ادرس کاربر")
    objects = MyUserManager()

    USERNAME_FIELD = "phone"

    def Created_at(self):
        return datetime2jalali(self.created_at)

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها "

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class OTP(models.Model):
    phone = models.CharField(max_length=30,null=True,blank=True)
    code = models.BigIntegerField(default=1,null=True)
    token = models.CharField(max_length=200, null=True, verbose_name="توکن کاربر")
    password = models.CharField(max_length=200, null=True, verbose_name="رمز کاربر")

    created_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ اضافه شدن")
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "otp"
        verbose_name_plural = "opts"


from product.models import Product
from customer.models import Customer


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    discription = models.TextField(max_length=300, null=True, blank=True, verbose_name="توضیحات مدیر")
    status = models.BooleanField(default=False)
    awnser = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True, verbose_name="تاریخ اضافه شدن")

    def created_data(self):
        return date2jalali(self.created_at)
    
    class Meta:
        verbose_name = "تیکت "
        verbose_name_plural = "تیکت ها"


