from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
# Create your views here.
from django.views.generic import View
from product.models import Product
from customer.models import Customer
from .models import InvoiceSale,ProductItemSale
# Create your views here.


class NewSaleView(View):
    def get(self,request):
        products = Product.objects.filter(user=request.user).filter(is_mojod=True)
        customers = Customer.objects.filter(user=request.user)

        return render(request,"sale/new.html",{"products":products,"customers":customers})


    def post(self,request):
        name_customer = request.POST.get("name_customer")
        get_customer = request.POST.get("get_customer")
        phone_customer = request.POST.get("phone_customer")
        names_product = request.POST.getlist("names_product")
        tedads = request.POST.getlist("tedad")
        discount = request.POST.get("discount")
        print(name_customer,get_customer,phone_customer)
        print(names_product)
        print(tedads)
        print(discount)
        item=0
        if name_customer:
            new_customer = Customer.objects.create(user=request.user,phone=phone_customer,fullname=name_customer)
            new_invoice = InvoiceSale.objects.create(user=request.user,customer=new_customer,off=int(discount))
        else:
            customer = Customer.objects.get(fullname=get_customer)
            new_invoice = InvoiceSale.objects.create(user=request.user,customer=customer,off=int(discount))
        for i in names_product:
            product = Product.objects.get(title=i)
            product.mojodi -= int(tedads[item])
            if product.mojodi == 0:
                product.is_mojod = False
            product_item = ProductItemSale.objects.create(user=request.user,product=product,price_selling=product.price_selling)
            product_item.tedad = int(tedads[item])
            product_item.price_kol = product_item.tedad * product_item.price_selling
            new_invoice.product.add(product_item)
            new_invoice.price_nahayi += product_item.price_kol
            new_invoice.last_price = new_invoice.price_nahayi - new_invoice.price_nahayi * int(discount)/100
           
            new_invoice.save()
            product.save()
            product_item.save()
            item +=1


        if name_customer:
                new_customer.price += new_invoice.last_price
                new_customer.price_mandeh += new_invoice.last_price
                if new_customer.price_mandeh != 0:
                    new_customer.is_paid = False
                else:
                    new_customer.is_paid = True
                new_customer.save()
        else:
                customer.price += new_invoice.last_price
                customer.price_mandeh += new_invoice.last_price
                if customer.price_mandeh != 0:
                    customer.is_paid = False
                else:
                    customer.is_paid = True
                customer.save()
        messages.success(request,"فروش جدید ثبت شد ")
        return redirect(f"/sale/detail/{new_invoice.id}")
    


class ListSaleView(View):
    def get(self,request):
        invoicesale = InvoiceSale.objects.filter(user=request.user)
        search_c = request.GET.get("search_c")
        if search_c:
            invoicesale = InvoiceSale.objects.filter(user=request.user).filter(customer__fullname__contains=search_c)
        return render(request,"sale/list.html",{"invoicesale":invoicesale ,"search_c":search_c})
    


class DetailSaleView(View):
    def get(self,request,*args,**kwargs):
        invoicesale = InvoiceSale.objects.filter(user=request.user)
        invoice = get_object_or_404(invoicesale,id=kwargs["id"])
        return render(request,"sale/detail.html",{"invoice":invoice})