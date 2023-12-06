from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("home")

    return render(request, "users/index.html")


def login(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user:
            auth_login(request, user)
            return redirect("home")

    return render(request, "users/login.html")


def logout(request):
    auth_logout(request)
    return redirect("index")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            user.save()
            auth_login(request, user)
            return redirect("home")

    return render(request, "users/signup.html")
