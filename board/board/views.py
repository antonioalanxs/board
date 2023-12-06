from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "board/home.html")

    return redirect("index")
