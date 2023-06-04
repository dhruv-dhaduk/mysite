from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "dhruv/index.html")

def headings(request):
    return render(request, "dhruv/headings.html")

def image(request):
    return render(request, "dhruv/image.html")

def button(request):
    return render(request, "dhruv/button.html")

def songs(request):
    return render(request, "dhruv/songs.html")

def resume(request):
    return render(request, "dhruv/resume.html")

def books(request):
    return render(request, "dhruv/books.html")

def counter(request):
    return render(request, "dhruv/counter.html")