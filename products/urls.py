from django.urls import include, path
from rest_framework import routers
from django.urls import include, path
from . import views


urlpatterns = [
    path("list_products", views.ProductsViewset.as_view(), name="list-products"),
]
