from django.urls import path 
from .import views 
app_name = "accounts"

urlpatterns = [
    path("dashboard/",views.DashboardView.as_view(),name="dashboard"),
    path("login/",views.LoginView.as_view(),name="login"),
    path("logout/",views.LogoutView.as_view(),name="logout")
]