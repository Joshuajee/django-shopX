from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Address, Cart
from django.contrib.auth import authenticate, login, logout
from shops.models import Order


# Create your views here.
def index(req):
    return render(req, "accounts/index.html")

def create_account(req):
    if req.method == "POST":
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        phone = req.POST['phone']
        address = req.POST['address']
        state = req.POST['state']
        

        try:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                phone = phone
            )

            Address.objects.create(user=user, state = state, address = address)

            login(req, user)

            return HttpResponseRedirect("/")
        except:
            print("error")
            pass

    return render(req, "accounts/create_account.html")


def login_view(req):

    if req.method == "POST":
        username=req.POST["username"]
        password=req.POST["password"]

        try:
            user= authenticate(username=username, password=password)

            if user == None:
                return render(req, "accounts/index.html"), {
                    'error' : "wrong username or password"
                }
            else:
                login(req, user)
                return HttpResponseRedirect("/")
        except:
            pass

    return render(req, "accounts/index.html")

def logout_view(req):
    logout(req)
    return HttpResponseRedirect("/")


def carts(req):

    user = req.user

    cart_items = Cart.objects.filter(user=user)

    print(cart_items)

    # user = User.objects.filter(product="product", quantity="quantity")
    # products  = Product.objects.filter(product="product")
    return render (req, "accounts/carts.html", {
        "cart_items" : cart_items
    })



