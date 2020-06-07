# urls.py - paths to different web pages
from django.urls import path

from . import views

urlpatterns = [
	path("", views.home, name = "home"),
]