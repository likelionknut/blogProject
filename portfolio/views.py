from django.shortcuts import render
from .models import Portfolio
# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects # 객체를 모두 가져옴
    return render(request, 'portfolio.html', {'portfolios' : portfolios})
    