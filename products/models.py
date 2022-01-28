from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Product model which can be accessed from Django Admin for create and update
class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "products"

    def __str__(self):
        return f"{self.name}-{self.price}"


# Purchase details model which can be accessed from Django Admin
class PurchaseDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    soft_delete = models.BooleanField(default=False)
    quantity = models.IntegerField()

    class Meta:
        db_table = "purchase_details"

    def __str__(self):
        return f"{self.user.username} Bought {self.quantity} {self.product.name}"
