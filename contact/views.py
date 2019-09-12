from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def contact(request):
    
    return render(request, "contact.html")
    
    



