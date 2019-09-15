from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.utils import timezone
from .models import Portfolio
from .forms import PortfolioForm


def portfolio(request):
    
    portfolio = PortfolioForm 
    
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save()
            messages.success(request, "Your Portfolio has been updated Successfully")
            return redirect(reverse('index'))
    else: 
        return render(request, 'portfolio.html',{"portfolio": portfolio})
