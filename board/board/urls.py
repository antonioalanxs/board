from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("create", views.create, name="create"),
    path("read/<uuid:slug>", views.read, name="read"),
    path("delete/<uuid:slug>", views.delete, name="delete"),
    path("update/<uuid:slug>", views.update, name="update"),
]
