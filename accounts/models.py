from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_vendor = models.BooleanField(default=False) 
    profile_img = models.FileField(upload_to="profiles", blank=True)
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    address = models.CharField(max_length=150)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("shops.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()