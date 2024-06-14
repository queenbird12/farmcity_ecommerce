from django.urls import path
from . import views

app_name = 'farmcityecommerce'

urlpatterns = [
    path('', views.home, name='home'),
    path(' ',views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_details'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>', views.customer_details, name='customer_details'),
]
