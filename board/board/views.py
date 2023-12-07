from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


from .models import Notice


# Create your views here.
@login_required
def home(request):
    """
    Fetch all notices from the database and render the home page displaying
    them. This view requires the user to be logged in.

    Args:
        request (`HttpRequest`): The HTTP request object.

    Returns:
        `HttpResponse`: Rendered home page with notices.
    """
    return render(
        request,
        "board/home.html",
        {"notices": Notice.objects.all()}
    )


@login_required
def create(request):
    """
    Handle the creation of a new notice. This view requires the user to be logged in.

    If the request method is `POST`, it creates a new `Notice` object with the provided title, content, and assigns the current user as the author. It then redirects to the home page.

    If the request method is `GET`, it renders the `board/create.html` template.

    Args:
        request (`HttpRequest`): The HTTP request object.

    Returns:
        `HttpResponse`: Rendered create page or redirects to home on successful notice creation.
    """
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
    """
    Render the page displaying a specific notice. This view requires the user to be logged in.

    Fetches a specific notice from the database based on the unique slug identifier and renders the `board/read.html` template displaying the details of it.

    Args:
        request (`HttpRequest`): The HTTP request object.
        slug (`str`): The `unique slug identifier` for the notice.

    Returns:
        `HttpResponse`: Rendered page with the specified notice.
    """
    return render(
        request,
        "board/read.html",
        {"notice": Notice.objects.get(slug=slug)}
    )


@login_required
def delete(request, slug):
    """
    Handle the deletion of a notice. This view requires the user to be logged in.

    Fetches a specific notice from the database based on the unique slug identifier. If the requesting user is the author of the notice, it deletes the notice and redirects to the home page. If not, it raises a `PermissionDenied` exception.

    Args:
        request (`HttpRequest`): The HTTP request object.
        slug (`str`): The `unique slug identifier` for the notice.

    Returns:
        `HttpResponse`: Redirects to home on successful notice deletion.

    Raises:
        `PermissionDenied`: If the requesting user is not the author of the notice.
    """
    notice = Notice.objects.get(slug=slug)

    if request.user != notice.author:
        raise PermissionDenied

    notice.delete()

    return redirect("home")


@login_required
def update(request, slug):
    """
    Handle the update of a notice. This view requires the user to be logged in.

    If the request method is `POST`, it updates the notice with the provided
    title and content and redirects to the home page. 

    If the request method is `GET`, it renders the `board/update.html` template.

    Args:
        request (`HttpRequest`): The HTTP request object.
        slug (`str`): The `unique slug identifier` for the notice.

    Returns:
        `HttpResponse`: Rendered update page or redirects to home on successful notice update.

    Raises:
        `PermissionDenied`: If the requesting user is not the author of the notice.
    """
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
