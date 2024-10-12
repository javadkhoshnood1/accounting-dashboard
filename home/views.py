from django.shortcuts import render,redirect
from django.views import View
# Create your views here.


class HomePageView(View):

    def get(self,request):
        if request.user.is_authenticated:
            return redirect("/dashboard/")
        else:
            return render(request,"home/index.html")