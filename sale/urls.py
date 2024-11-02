from django.urls import path
from .import views
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

app_name= "sale"

urlpatterns = [
    path("new/",login_required(views.NewSaleView.as_view()),name="new_sale"),
    path("list/",login_required(views.ListSaleView.as_view()),name="list_sale"),
    path("detail/<int:id>/",login_required(views.DetailSaleView.as_view()),name="detail_sale")

]