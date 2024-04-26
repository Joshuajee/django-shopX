from django.db import models
from accounts.models import User

# Create your models here.

class Status(models.TextChoices):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.FileField(upload_to="uploads/products")
    quantity = models.IntegerField()
    description = models.TextField()
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=540)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    # where the product is comming from
    source_state = models.CharField(max_length=50)
    source = models.CharField(max_length=150)
    # where the product is going to
    destination_state = models.CharField(max_length=50)
    destination = models.CharField(max_length=150)
    
    status = models.CharField(max_length=50, choices=Status, default=Status.PENDING)
    
