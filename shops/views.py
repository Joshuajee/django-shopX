from django.shortcuts import render
from .models import Status, Product, Review, Order


# Create your views here.
def index(req):
    products  = Product.objects.all()
    return render (req, "index.html",{
                        "products":products})

def product(req, id):
    return render (req, "index.html") 