from django.contrib import admin
from .models import  User, Address, Cart


# Register your models here.
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Cart)