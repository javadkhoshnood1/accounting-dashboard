from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "customer"

urlpatterns = [
    path("list/",login_required(views.ListCustomerView.as_view()),name="list_customer"),
    path("detail/<int:id>/",login_required(views.DetailCustomerView.as_view()),name="detail_customer"),
    path("delete/<int:id>/",login_required(views.DeleteCustomerView.as_view()),name="delete_customer"),
]