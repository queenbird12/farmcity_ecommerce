from django.shortcuts import get_object_or_404,render
from .models import Product
from .models import Customer

# Create your views here.
def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = Product.objects.all()
    context= {
        'products': products
    }
    return render(request,'farmcityecommerce/product_list.html', context)

def product_detail(request, pk):
    product =get_object_or_404(Product, pk=pk)
    context= {
        'product': product
    }
    return render(request, 'farmcityecommerce/product_details', context)

def customer_list(request, pk):
    Customers = Customer.objects.all()
    context= {
        'customers': Customers
    }
    return render(request,'./templates/farmcityecommerce/customer_list.html', context)

def customer_details(request, pk):
    Customer = get_object_or_404(Customer, pk=pk)
    context= {
        'customer': Customer
    }
    return render(request, './templates/farmcityecommerce/customer_details', context)