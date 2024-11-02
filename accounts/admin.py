from django import forms
from django.contrib import admin

from accounts.models import User,OTP,Ticket


@admin.register(User)
class UserRegister(admin.ModelAdmin):
    list_display = ("phone", "fullname", "is_admin")
    
    
    
    
@admin.register(OTP)
class OTPRegister(admin.ModelAdmin):
    list_display = ("phone", "code")

@admin.register(Ticket)
class TicketRegister(admin.ModelAdmin):
    list_display = ("user", "title",'status')