from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.utils import timezone
from .models import Portfolios
from .forms import PortfolioForm


def all_portfolios(request):
    portfolios = Portfolios.objects.all()
    return render(request, "portfolio.html", {"portfolios": portfolios})
    

def portfolios(request):
    
    portfolios = PortfolioForm 
    
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolios = form.save()
            messages.success(request, "Your Portfolio has been added Successfully")
            return redirect(reverse('index'))
    else: 
        return render(request, 'portfolio.html',{"portfolios": portfolios})
