from django.urls import path
from . import views
from farmcityecommerce.views import home
from farmcityecommerce.views import cart

app_name = 'farmcityecommerce'

urlpatterns = [
    path("", home, name='home'),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("main/", views.checkout, name="main"),
]
