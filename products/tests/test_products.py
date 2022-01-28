import pytest
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from graphene.test import Client
from bookrCommerce.schema import schema
from mixer.backend.django import mixer
from products.models import Product
from products.serializers import ProductSerializer
from bookrCommerce.queries import (
    PRODUCTS_QUERY,
    PRODUCTS_QUERY_NAME,
    CREATE_PRODUCT_QUERY,
    UPDATE_PRODUCT_QUERY,
)
from rest_framework import status

# Unit Testing for GraphQL queries for products CRUD
@pytest.mark.django_db
class ProductGraphQLUnitTestCase(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.product = mixer.blend(Product)

    def test_products_listing(self):

        response = self.client.execute(PRODUCTS_QUERY)
        products = response.get("data").get("products")
        assert len(products)

    def test_product_by_name(self):
        response = self.client.execute(
            PRODUCTS_QUERY_NAME, variable_values={"name": self.product.name}
        )
        product_by_name = response.get("data").get("productByName")
        assert product_by_name["name"] == str(self.product.name)

    def test_create_product(self):
        payload = {"name": "Choclate", "price": "10.1", "description": "123"}
        response = self.client.execute(
            CREATE_PRODUCT_QUERY, variable_values={"input": payload}
        )
        product = response.get("data").get("create_product").get("product")
        name = product.get("name")
        assert name == payload["name"]

    def test_update_product(self):
        payload = {
            "name": "updated name",
            "price": "10.1",
            "description": "testing description",
        }
        response = self.client.execute(
            UPDATE_PRODUCT_QUERY,
            variable_values={"id": self.product.id, "input": payload},
        )
        product = response.get("data").get("update_product").get("product")
        name = product.get("name")
        assert name == payload["name"]
        assert name != self.product.name


# Unit testing for product listing DRF endpoint.
@pytest.mark.django_db
class ProductAPIUnitTestCase(APITestCase):
    def setUp(self):
        self.product = mixer.blend(Product)

    def test_product_list_endpoint(self):
        response = self.client.get(reverse("list-products"))
        # Get the faked data to assert from the DB
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
