from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView
from django.views import View
# Create your views here.
from django.contrib import messages
from .models import User
from django.contrib.auth import login,logout,authenticate
from .models import Ticket
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






    


class TicketView(View):
    def get(self,request):
        tickets = Ticket.objects.filter(user=request.user)

        return render(request,"accounts/tickets.html",{"tickets":tickets})
    

    def post(self,request):
        title = request.POST.get("title")
        discription = request.POST.get("discription")
        if title and discription:
            Ticket.objects.create(user=request.user,title=title,discription=discription)
            messages.success(request,"تیکت شما ثبت شد . منتشر پاسخ باشید ")
            return redirect("/tickets/")
        else:
            messages.error(request,"تیکت شما ثبت نشد ")
            return redirect("/tickets/")
        



class TicketDetailView(View):
    def get(self,request,*args,**kwargs):
        tickets = Ticket.objects.filter(user=request.user)
        ticket = get_object_or_404(tickets,id=kwargs["id"])
        return render(request,"accounts/ticket_detail.html",{"ticket":ticket})

        


class EditProfileView(View):
    def get(self,request):
        return render(request,"accounts/edit_profile.html")
    
    def post(self,request):
        fullname = request.POST.get("fullname")
      
        name_shop = request.POST.get("name_shop")
        email = request.POST.get("email")
        discription = request.POST.get("discription")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if fullname and name_shop and email and discription:
            request.user.fullname = fullname
            request.user.name_shop = name_shop
            request.user.email = email
            request.user.discription = discription
            request.user.save()
            if password1 and password2:
                if password1 == password2:
                    request.user.set_password(password1)
                    request.user.save()
                else:
                    messages.error(request,"رمز عبور شما مشابه هم نیست ")
                    return redirect("/edit-profile/")
        messages.success(request,"اطلاعات کاربری شما با موفقیت ویرایش شد !")
        return redirect("/edit-profile/")