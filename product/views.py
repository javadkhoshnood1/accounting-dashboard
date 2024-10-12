from django.shortcuts import render,redirect
from django.views.generic import TemplateView
# Create your views here.
from .models import Product,Category
from django.views import View
from django.contrib import messages
class ListProductView(TemplateView):
    template_name = "product/list.html"

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(user=request.user)
        categories = Category.objects.filter(user=request.user)

        return render(request,"product/list.html",{"products":products,"categories":categories})
    


class CtegoriesView(TemplateView):
    template_name = "product/categories.html"
    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(user=request.user)

        return render(request,"product/categories.html",{"categories":categories}) 


class AddCatgeory(View):
    def post(self,request):
        title = request.POST.get("title")
        discription = request.POST.get("discription")
        if title and discription:
            Category.objects.create(user=request.user,title=title,discription=discription)
            messages.success(request,"دسته بندی جدید اضافه شد ")
            return redirect("/product/list/")
        else:
            messages.error(request,"عملیات ناموفق ")
            return redirect("/product/list/")
