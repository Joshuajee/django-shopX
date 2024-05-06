from django.shortcuts import render
from .models import Status, Product, Review, Order


# Create your views here.
def index(req):
    products  = Product.objects.all()
    return render (req, "index.html",{
                        "products":products})

def product(req, id):
    product_details = Product.objects.get(id=id)
    print(id)
    return render (req, "product.html",
                         {"product":product_details}) 

def about(req):
    return render (req, "about.html")

def contact(req):
    return render (req, "contact.html")

def cart(req):
    return render (req, "cart.html")


