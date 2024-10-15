from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
# Create your views here.
from django.views.generic import View
from product.models import Product
from .models import InvoiceShop,ProductItem


class NewShopView(View):
    def get(slef,request,*args,**kwargs):
        products = Product.objects.filter(user=request.user)

        return render(request,"shopping/new.html" ,{"products":products})
    
    def post(self,request,*args,**kwargs):
        products = Product.objects.filter(user=request.user)

        name_shekat = request.POST.get("name_shekat")
        phone = request.POST.get("phone")
        names = request.POST.getlist("name")
        prices = request.POST.getlist("price")
        tedads = request.POST.getlist("tedad")
        discount = request.POST.get("discount")
        kerayeh = request.POST.get("kerayeh")
        item =0
        new_invoice = InvoiceShop.objects.create(user=request.user,name_company=name_shekat,phone_company=phone,off=int(discount),keriyeh=int(kerayeh))
        for name_products in names:
            if Product.objects.filter(user=request.user).filter(title__contains=name_products).exists():
                select_product =Product.objects.filter(user=request.user).get(title__contains=name_products)
                new_item = ProductItem.objects.create(user=request.user,product=select_product,price=int(prices[item]),tedad=int(tedads[item]),price_kol=int(prices[item])*int(tedads[item]))
                new_invoice.product.add(new_item)
                new_invoice.price_nahayi += int(prices[item]) * int(tedads[item])
                new_invoice.save()
                select_product.mojodi += int(tedads[item])
                select_product.price = int(prices[item])
                select_product.price_selling = int(prices[item])
                if int(tedads[item]) !=0:
                    select_product.is_mojod = True
                if select_product.percent_sod != 0:
                    select_product.price_selling = int(prices[item]) + int(prices[item]) * int(select_product.percent_sod)/100
                    select_product.sod = select_product.price_selling - select_product.price    
                select_product.save()
            else:
                new_select_product = Product.objects.create(user=request.user,title=name_products,price=int(prices[item]),price_selling=int(prices[item]))
                new_select_product.mojodi += int(tedads[item])
                if int(tedads[item]) !=0:
                    new_select_product.is_mojod = True
                if new_select_product.percent_sod != 0:
                    new_select_product.price_selling = int(prices[item]) + int(prices[item]) * int(new_select_product.percent_sod)/100
                    new_select_product.sod = new_select_product.price_selling - new_select_product.price    
                new_select_product.save()             
                new_itemm = ProductItem.objects.create(user=request.user,product=new_select_product,price=int(prices[item]),tedad=int(tedads[item]),price_kol=int(prices[item])*int(tedads[item]))
                new_invoice.product.add(new_itemm)
                new_invoice.price_nahayi += int(prices[item]) *int(tedads[item])

                new_invoice.save()
            item +=1
        new_invoice.last_price =   int(new_invoice.price_nahayi) - int(new_invoice.price_nahayi) * int(new_invoice.off)/100
        new_invoice.last_price += int(new_invoice.keriyeh) 
        new_invoice.save()
        messages.success(request,"بار جدید ثبت شد ")
        return redirect("/shopping/list")


class listShopView(View):
    def get(self,request):
        invoiceshops = InvoiceShop.objects.filter(user=request.user)
        return render(request,"shopping/list.html",{"invoiceshops":invoiceshops})
    

class DetailShopView(View):
    def get(self,request,*args,**kwargs):
        invoiceshops = InvoiceShop.objects.filter(user=request.user)
        invoice = get_object_or_404(invoiceshops,id=kwargs["id"])
        return render(request,"shopping/detail.html",{"invoice":invoice})
