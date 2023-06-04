from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("headings", views.headings, name="headings"),
    path("image", views.image, name="image")
]