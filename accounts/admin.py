from django import forms
from django.contrib import admin

from accounts.models import User,OTP


@admin.register(User)
class UserRegister(admin.ModelAdmin):
    list_display = ("phone", "fullname", "is_admin")
    
    
    
    
@admin.register(OTP)
class OTPRegister(admin.ModelAdmin):
    list_display = ("phone", "code")