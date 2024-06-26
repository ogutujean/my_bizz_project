from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
   

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products' , on_delete=models.CASCADE)
    stock = models.PositiveIntegerField( default=0 )
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='uploads/products', null=True, blank=True)
    

    def __str__(self):
        return f"{self.name} of {self.description} at a price of {self.price}"
    
    