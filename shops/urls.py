from django.urls import path
from .views import index, product

urlpatterns = [ 
    path("", index), 
    path("product/<int:id>", product)
]





