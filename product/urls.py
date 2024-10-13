from django.urls import path
from .import views
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

app_name ="product"

urlpatterns =[
    path("list/",login_required(views.ListProductView.as_view(),),name="list_p"),
    path("categories/list",login_required(views.CtegoriesView.as_view(),),name="list_p_c"),
    path("categories/add",login_required(views.AddCatgeory.as_view(),),name="add_catgeory"),
    path("categories/delete/<int:id>",login_required(views.DeleteCatgeory.as_view(),),name="delete_catgeory"),
    path("delete/<int:id>/",login_required(views.DeleteProductView.as_view(),),name="delete_p"),
    path("detail/<int:id>/",login_required(views.DetailProductView.as_view(),),name="detail_p"),
]