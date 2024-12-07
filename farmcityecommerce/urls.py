from django.urls import path
from . import views
from farmcityecommerce.views import home
from farmcityecommerce.views import cart

app_name = 'farmcityecommerce'

urlpatterns = [
    path("", home, name='home'),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("updateitem/", views.updateItem, name="updateitem"),
    path("product/<int:pk>", views.product, name="product"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("process_order/", views.processOrder, name="process_order"),
]