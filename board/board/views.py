from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "board/index.html")

    return HttpResponseRedirect(reverse("login"))
