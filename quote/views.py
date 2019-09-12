from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.utils import timezone
from .models import Quote
from .forms import GetQuote

def quote(request):
    
    quote = GetQuote 
    
    if request.method == "POST":
        form = GetQuote(request.POST)
        if form.is_valid():
            quote = form.save()
            messages.success(request, "Thank you for your Quotation Request which has been sent sucessfully. We will be in touch soon.")
            return redirect(reverse('index'))
    else: 
        return render(request, 'quote.html',{"quote": quote})
 
        
    
        
    