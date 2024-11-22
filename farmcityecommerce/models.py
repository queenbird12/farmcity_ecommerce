from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
     user = models.OneToOneField(User,on_delete= models.CASCADE,null=True, blank=True)
     first_name = models.CharField(max_length=50)
     last_name =models.CharField(max_length=50)
     email = models.EmailField(unique=True)
     phone= models.CharField(max_length=13, blank=True, null=True)
     address= models.CharField(max_length=100, blank=True, null=True)
     created_when = models.DateTimeField(auto_now_add= True)

     def __str__(self):
         return  f"{self.first_name} {self.last_name} {self.email}"
     
class Product(models.Model):
    name = models.CharField(max_length=300,null=True)
    description= models.TextField()
    price= models.FloatField()
    Availability = models.BooleanField(default=False,null=True,blank=False)
    image = models.ImageField(upload_to='product/' ,null=True, blank=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered= models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 
    
class OrderItem(models.Model):
     product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
     quantity = models.IntegerField(default=0, null=True, blank=True)
     date_added = models.DateTimeField(auto_now_add=True)

     @property
     def get_total(self):
         total = self.product.price * self.quantity
         return total


class ShippingAddress(models.Model):
     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
     address= models.CharField(max_length=100, null=True)
     city= models.CharField(max_length=100, null=True)
     county= models.CharField(max_length=100, null=True)
     town= models.CharField(max_length=100, null=True)
     date_added = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
         return self.address
