from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    products =Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'farmcityecommerce/home.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items= order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context= {'items': items,'order':order}
    return render(request, 'farmcityecommerce/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items= order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context= {'items': items,'order':order}
    return render(request, 'farmcityecommerce/checkout.html',context)

def main(request):
    context = {}
    return render(request, 'farmcityecommerce/main.html',context)
