from django.urls import path 
from .import views 
from django.contrib.auth.decorators import login_required, permission_required
app_name = "about"

urlpatterns =[
    path("",login_required(views.GuidanceUsView.as_view()),name="guidance-us")
]