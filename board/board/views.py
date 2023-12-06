from django.shortcuts import render
from django.shortcuts import redirect

from .models import Notice


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "board/home.html", {"notices": Notice.objects.all()})

    return redirect("index")


def notice(request):
    if not request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        notice = Notice(
            title=request.POST["title"],
            content=request.POST["content"],
            author=request.user,
        )
        notice.save()
        return redirect("home")

    return render(request, "board/create.html")


def notice_detail(request, slug):
    if not request.user.is_authenticated:
        return redirect("index")

    return render(
        request,
        "board/notice.html",
        {"notice": Notice.objects.get(slug=slug)}
    )
