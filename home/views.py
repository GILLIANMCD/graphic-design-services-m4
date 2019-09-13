from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


