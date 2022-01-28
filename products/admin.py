from django.contrib import admin
from .models import Product, PurchaseDetails

# Register your models here.

admin.site.register(Product)
admin.site.register(PurchaseDetails)
