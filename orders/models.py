from django.db import models
from products.models import Product
from django.contrib.auth.models import User



# class Order(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     ordered_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.quantity} of {self.product.name} ordered on {self.ordered_date}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    total = models.DecimalField(max_digits=10, decimal_places=2,  default=0  )
    ordered_date = models.DateTimeField(auto_now_add=True)
   
  

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipping_address')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)