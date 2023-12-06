from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Notice


# Create your views here.
@login_required
def home(request):
    return render(request, "board/home.html", {"notices": Notice.objects.all()})


@login_required
def notice(request):
    if request.method == "POST":
        notice = Notice(
            title=request.POST["title"],
            content=request.POST["content"],
            author=request.user,
        )
        notice.save()
        return redirect("home")

    return render(request, "board/create.html")


@login_required
def notice_detail(request, slug):
    return render(
        request,
        "board/notice.html",
        {"notice": Notice.objects.get(slug=slug)}
    )
