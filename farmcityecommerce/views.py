import json
import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages

#from django.db.utils import IntegrityError


from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"hey{user} ,your account was created")
            return redirect('farmcityecommerce:login')  
            
    context = {'form':form}
    return render(request, 'farmcityecommerce/register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to 'next' or homepage
            return redirect('farmcityecommerce:home')
        else: 
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'farmcityecommerce/login.html',context)

def logoutUser(request):
    return redirect('farmcityecommerce:login')

def home(request):
    # Fetch all products to display on the homepage
    products = Product.objects.all()

    cartItems = 0  # Default value for cart items

    if request.user.is_authenticated:
        try:
            # Fetch the customer object for the authenticated user
            customer = request.user.customer
        except Customer.DoesNotExist:
            # Create a customer object if it doesn't exist
            customer = Customer.objects.create(user=request.user, email=request.user.email)

        # Get or create an order for the customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        # Fetch all items in the current order
        items = order.orderitem_set.all()

        # Update cart items count from the order
        cartItems = order.get_cart_items
    else:
        # For unauthenticated users, provide default values
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    # Pass data to the template
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'farmcityecommerce/home.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items= order.orderitem_set.all()
        cartItems = order.get_cart_items
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
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context= {'items': items,'order':order}
    return render(request, 'farmcityecommerce/checkout.html',context)

def main(request):
    context = {}
    return render(request, 'farmcityecommerce/main.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:',action)
    print('productId',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete= False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity =(orderItem.quantity -1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('ITEM WAS ADDED', safe=False)

def processOrder(request):
    transaction_id= datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        total = float (data['form']['total'])
        order.transction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
            order.save()
            if order.shipping:
                ShippingAddress.objects.create(
                    customer=customer,
                    order=order,
                    address=data['shipping']['address'],
                    city=data['shipping']['city'],
                    county=data['shipping']['county'],
                    town=data['shipping']['town'],
                )
    else:
        print('user is not logged in')
    return JsonResponse('payment complete!', safe=False)