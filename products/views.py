from django.shortcuts import render
from rest_framework import mixins, generics
from .models import Product, PurchaseDetails
from .serializers import ProductSerializer

# Create your views here.


# Endpoint to list the created Products from Django Admin or from PostgreSQL
class ProductsViewset(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
