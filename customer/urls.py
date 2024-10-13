from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "customer"

urlpatterns = [
    path("list/",login_required(views.ListCustomerView.as_view()),name="list_customer"),
]