from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views import View
# Create your views here.
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

class DashboardView(TemplateView):
    template_name = "accounts/dashborad.html"



class LoginView(View):
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"ورود با موفقیت انجام شد ")
            return redirect("/dashboard")
        else:
            messages.error(request,"کاربر با اطلاعات شما یافت نشد ")
            return redirect("/")
        
class LogoutView(View):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request,"خروج با موفقیت انجام شد ")
            return redirect("/")
        else:
            messages.error(request,"عملیات ناموفق")
            return redirect("/")
