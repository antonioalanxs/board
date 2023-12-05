from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "users/index.html")
        
    return HttpResponseRedirect(reverse("login"))

def login(request):
    if request.user.is_authenticated:
        return render(request, "users/index.html")
    
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        
    return render(request, "users/login.html")

def logout(request):
    auth_logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
