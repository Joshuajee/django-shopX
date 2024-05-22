from django.urls import path
from .views import index, product, contact, about, cart, addtocart,order, checkout

urlpatterns = [ 
    path("", index), 
    path("product/<int:id>", product),
    path("about", about),
    path("contact", contact),
    path("cart", cart),
    path("addtocart", addtocart),
    path("order", order),
    path("checkout", checkout)
]





