from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

def contact(request):
    
    contact = ContactForm
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, "Thank you for your Enquiry which has been sent sucessfully. We will be in touch soon.")
            return redirect(reverse('index'))
    else: 
        return render(request, 'contact.html', {"contact": contact})
    
    



