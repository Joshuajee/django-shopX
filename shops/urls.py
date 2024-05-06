from django.urls import path
from .views import index, product, contact, about, cart

urlpatterns = [ 
    path("", index), 
    path("product/<int:id>", product),
    path("about", about),
    path("contact", contact),
    path("cart", cart),
]





