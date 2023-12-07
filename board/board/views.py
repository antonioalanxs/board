from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


from .models import Notice


# Create your views here.
@login_required
def home(request):
    return render(request, "board/home.html", {"notices": Notice.objects.all()})


@login_required
def create(request):
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
def read(request, slug):
    return render(
        request,
        "board/read.html",
        {"notice": Notice.objects.get(slug=slug)}
    )


@login_required
def delete(request, slug):
    notice = Notice.objects.get(slug=slug)

    if request.user != notice.author:
        raise PermissionDenied

    notice.delete()

    return redirect("home")


@login_required
def update(request, slug):
    notice = Notice.objects.get(slug=slug)

    if request.user != notice.author:
        raise PermissionDenied

    if request.method == "POST":
        notice.title = request.POST["title"]
        notice.content = request.POST["content"]
        notice.save()
        return redirect("home")

    return render(
        request,
        "board/update.html",
        {"notice": notice}
    )
