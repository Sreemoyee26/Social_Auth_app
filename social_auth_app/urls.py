from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("home/", views.home, name="home"),
]