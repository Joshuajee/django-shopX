from django.shortcuts import render
from .models import Status, Product, Review, Order
from accounts.models import Cart


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
    user = req.user
    quantity = req.POST["no_of_items"]
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
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
    

