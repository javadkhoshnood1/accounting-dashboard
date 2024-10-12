from django.urls import path 
from .import views 
from django.contrib.auth.decorators import login_required, permission_required
app_name = "accounts"

urlpatterns = [
    path("dashboard/",login_required(views.DashboardView.as_view()),name="dashboard"),
    path("login/",views.LoginView.as_view(),name="login"),
    path("logout/",views.LogoutView.as_view(),name="logout")
]