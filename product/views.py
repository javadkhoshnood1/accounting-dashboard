from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView
# Create your views here.
from .models import Product,Category
from django.views import View
from django.contrib import messages
class ListProductView(TemplateView):
    template_name = "product/list.html"

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(user=request.user)
        categories = Category.objects.filter(user=request.user).order_by("-created_at")
        search_p = request.GET.get("search_p")
        available = request.GET.get("available")
        unavailable = request.GET.get("unavailable")
        if available:
            products = Product.objects.filter(user=request.user).filter(is_mojod=True)
        if unavailable:
            products = Product.objects.filter(user=request.user).filter(is_mojod=False)
        if search_p  :
            products = Product.objects.filter(user=request.user).filter(title__contains=search_p)
            messages.success(request,f"{products.count()} عدد محصول یافت شد ")

        return render(request,"product/list.html",{"products":products,"categories":categories ,"search_p":search_p ,"available":available,"unavailable":unavailable})
    

    def post(self,request):
        categorys = Category.objects.all().filter(user=request.user)
        title = request.POST.get("title")
        price = request.POST.get("price")
        percent = request.POST.get("percent")
        category = request.POST.get("category")
        catgeory_select = get_object_or_404(categorys,id=category)
        if title and price and percent and category:
            if Product.objects.filter(user=request.user).filter(title__contains=title):
                messages.error(request,"این محصول در لیست محصولات  وجود دارد !")
                return redirect("/product/list/")
            else:
                new_product = Product.objects.create(user=request.user,category=catgeory_select,title=title,price=int(price),percent_sod=int(percent))
                new_product.price_selling = int(price) + int(price) * int(percent)/100
                new_product.sod = new_product.price_selling - new_product.price
                new_product.save()
                messages.success(request,"محصول جدید شما اضافه شد !")
                return redirect(f"/product/list/")

class CtegoriesView(TemplateView):
    template_name = "product/categories.html"
    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(user=request.user).order_by("-created_at")
        search_c = request.GET.get("search_c")
        if search_c  :
            categories = Category.objects.filter(user=request.user).filter(title__contains=search_c)
            messages.success(request,f"{categories.count()} عدد دسته بندی  یافت شد ")
        return render(request,"product/categories.html",{"categories":categories,"search_c":search_c}) 


class AddCatgeory(View):
    def post(self,request):
        title = request.POST.get("title")
        discription = request.POST.get("discription")
        if title and discription:
            Category.objects.create(user=request.user,title=title,discription=discription)
            messages.success(request,"دسته بندی جدید اضافه شد ")
            return redirect("/product/categories/list")
        else:
            messages.error(request,"عملیات ناموفق ")
            return redirect("/product/categories/list")
        

class DeleteCatgeory(View):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.filter(user=request.user).order_by("-created_at")
        category = get_object_or_404(categories,id=kwargs["id"])
        messages.success(request,f"دسته بندی {category.title} حذف شد ")
        category.delete()
        return redirect("/product/categories/list")



class DeleteProductView(View):
    def get(self,request,*args,**kwargs):
        products = Product.objects.filter(user=request.user)
        product = get_object_or_404(products,id=kwargs["id"])
        messages.success(request,f"محصول {product.title} حذف شد ! ")
        product.delete()
        return redirect("/product/list")


class DetailProductView(View):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.filter(user=request.user).order_by("-created_at")

        products = Product.objects.filter(user=request.user)
        product = get_object_or_404(products,id=kwargs["id"])
        return render(request,"product/detail.html",{"product":product,"categories":categories})
    

    def post(self,request,*args,**kwargs):
        categories = Category.objects.filter(user=request.user)

        products = Product.objects.filter(user=request.user)
        product = get_object_or_404(products,id=request.POST.get("id"))
        title = request.POST.get("title")
        percent_sod = request.POST.get("percent_sod")
        discription = request.POST.get("discription")
        category = request.POST.get("category")
        catgeory_select = get_object_or_404(categories,id=category)
        if category:
            product.category = catgeory_select
        product.title = title
        product.percent_sod = int(percent_sod)
        product.discription = discription
        product.price_selling = product.price+ product.price * int(percent_sod)/100
        product.sod = product.price_selling - product.price
        product.save()
        messages.success(request,f"محصول {product.title}ویرایش شد  ")
        return redirect("/product/list")
    