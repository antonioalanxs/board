from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("notice", views.notice, name="notice"),
    path("notice/<uuid:slug>", views.notice_detail, name="notice_detail"),
]
