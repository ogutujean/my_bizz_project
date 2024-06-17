from django.db import models
from products.models import Product
from django.conf import settings


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField( default=1 )

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

