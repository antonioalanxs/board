from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """
    Render the index page.

    Args:
        request (`HttpRequest`): The HTTP request object.

    Returns:
        `HttpResponse`: Rendered index page.
    """
    return render(request, "users/index.html")


def login(request):
    """
    Handle user login.

    If the user is already authenticated, it redirects to the home page.

    If the request method is `POST`, it authenticates the user with the provided username and password and redirects to the home page.

    If the request method is `GET`, it renders the `users/login.html` template.

    Args:
        request (`HttpRequest`): The HTTP request object.

    Returns:
        `HttpResponse`: Rendered login page or redirects to home on successful login.
    """
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user:
            auth_login(request, user)
            return redirect(request.POST["next"] or "home")

    return render(request, "users/login.html")


@login_required
def logout(request):
    """
    Handle user logout. This view requires the user to be logged in.

    Args:
        request (`HttpRequest`): The HTTP request object.

    Returns:
        `HttpResponse`: Redirects to index page.
    """
    auth_logout(request)
    return redirect("index")


def signup(request):
    """
    Handle user signup.

    If the request method is `POST`, it creates a new user with the provided username and password and redirects to the home page.

    If the request method is `GET`, it renders the `users/signup.html` template.

    Args:
        request (`HttpRequest`): The HTTP request object.

    Returns:
        `HttpResponse`: Rendered signup page or redirects to home on successful signup.
    """
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
