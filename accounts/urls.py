from django.urls import path 
from .import views 
from django.contrib.auth.decorators import login_required, permission_required
app_name = "accounts"

urlpatterns = [
    path("dashboard/",login_required(views.DashboardView.as_view()),name="dashboard"),
    path("tickets/",login_required(views.TicketView.as_view()),name="tickets"),
    path("tickets/<int:id>/",login_required(views.TicketDetailView.as_view()),name="ticket-detail"),
    path("edit-profile/",login_required(views.EditProfileView.as_view()),name="edit-profile"),
    path("login/",views.LoginView.as_view(),name="login"),
    path("logout/",views.LogoutView.as_view(),name="logout")
]