from django.urls import path 
from . import views
from django.contrib.auth.decorators import login_required

app_name = "shopping"

urlpatterns = [
    path("new/",login_required(views.NewShopView.as_view()),name="new_shop"),
    path("list/",login_required(views.listShopView.as_view()),name="list_shop"),
    path("detail/<int:id>/",login_required(views.DetailShopView.as_view()),name="detail_shop")
]