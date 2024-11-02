from django.shortcuts import render
from django.views import View
# Create your views here.
from django.contrib import messages

class GuidanceUsView(View):
    def get(self,request):
        return render(request,"about/guidance_us.html")