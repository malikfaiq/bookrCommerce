from rest_framework import serializers
from .models import Product, PurchaseDetails


# Product and Purchase Serializers to handle json serialization of objects while sending and receiving data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]


class PurchaseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDetails
        fields = "__all__"
