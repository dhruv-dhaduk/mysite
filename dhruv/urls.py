from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("headings", views.headings, name="headings"),
    path("image", views.image, name="image"),
    path("button", views.button, name="button"),
    path("songs", views.songs, name="songs"),
    path("resume", views.resume, name="resume"),
    path("books", views.books, name="books"),
    path("counter", views.counter, name="counter")
]