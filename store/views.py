from django.shortcuts import render, redirect
from . models import Customer, Product, Cart, Cartitems, Location
from django.http import JsonResponse
import json
from django.contrib import messages

def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}
    """ banner = BannerProduct.objects.order_by('-id') """
    banner_include = Product.objects.filter(banner_include=True).order_by('-id')
    products = Product.objects.order_by('id').filter(combo=False)
    combo = Product.objects.filter(combo=True).order_by('id')
    highlight_include = Product.objects.filter(highlight_include=True).order_by('id')
    locations = Location.objects.all()
    return render (request, 'store.html', {
        'products': products, 
        'cart': cart, 
        'combo': combo, 
        'banner_include': banner_include,
        'highlight_include': highlight_include,
        'locations': locations,
        })


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}


    return render(request, 'cart.html', {'cartitems' : cartitems, 'cart':cart})


def checkout(request):
    return render(request, 'checkout.html', {})

def updateCart(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
    cartitem, created = Cartitems.objects.get_or_create(cart = cart, product = product)

    if action == "add":
        cartitem.quantity += 1
        """ messages.add_message(request, messages.SUCCESS, 'Produto adicionado ao carrinho') """
        cartitem.save()

    return JsonResponse("Cart Updated", safe = False)
    """ return JsonResponse("Cart Updated", safe = False) """



def updateQuantity(request):
    data = json.loads(request.body)
    quantityFieldValue = data['qfv']
    quantityFieldProduct = data['qfp']
    product = Cartitems.objects.filter(product__name = quantityFieldProduct).last()
    product.quantity = quantityFieldValue
    product.save()
    return JsonResponse("Quantity updated", safe = False)

def productinfo(request, product_id):
    product_info = Product.objects.get(id=product_id)
    return render(request, 'productinfo.html', {'product_info':product_info})

def search(request):
    search_perfume = Product.objects.filter(name__icontains = request.POST.get('name_of_perfume'))
    return render (request, 'search.html', {'search_perfume': search_perfume})