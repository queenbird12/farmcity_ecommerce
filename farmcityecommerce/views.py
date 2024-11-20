from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Product
from .models import Customer

# Create your views here.
def home(request):
    return render(request, 'farmcityecommerce/home.html')

def cart(request):
    context= {}
    return render(request, 'farmcityecommerce/cart.html',context)

def checkout(request):
    context = {}
    return render(request, 'farmcityecommerce/checkout.html',context)

def main(request):
    context = {}
    return render(request, 'farmcityecommerce/main.html',context)
