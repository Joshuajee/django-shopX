from django.shortcuts import render
from .models import Status, Product, Review, Order
from accounts.models import Cart
from django.http import HttpResponse, HttpResponseRedirect



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

def addtocart(req):
    productid = req.POST["product"]
    product = Product.objects.get(id=productid)
    user = req.user
    quantity = req.POST["no_of_items"]
    Cart.objects.create(user=user, quantity=quantity, product=product)

    return HttpResponseRedirect("account/carts")
def order(req):
    return render (req, "order.html")

def checkout(req):
    return render (req, "checkout.html")

    
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    #  if req.method == "POST":
    #     username=req.POST["username"]
    #     password=req.POST["password"]

    #     try:
    #         user= authenticate(username=username, password=password)

    #         if user == None:
    #             return render(req, "accounts/index.html"), {
    #                 'error' : "wrong username or password"
    #             }
    #         else:
    #             login(req, user)
    #             return HttpResponseRedirect("/")
    #     except:
    #         pass

    # return render(req, "accounts/index.html")
    

