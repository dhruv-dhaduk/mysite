from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "dhruv/index.html")

def headings(request):
    return render(request, "dhruv/headings.html")