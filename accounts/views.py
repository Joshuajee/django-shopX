from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, "accounts/index.html")

def create_account(req):
    if req.method == "POST":
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        

        try:
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
                
                )
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




