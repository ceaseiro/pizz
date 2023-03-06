from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart', views.cart, name='cart'),
    path('<int:product_id>', views.productinfo, name='productinfo'),
    path('checkout', views.checkout, name='checkout'),
    path('updatecart', views.updateCart, name='updatecart'),
    path('updatequantity', views.updateQuantity, name='updatequantity'),
    path('search', views.search, name='search'),
]