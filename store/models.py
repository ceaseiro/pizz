from django.db import models
from django.contrib.auth.models import User
import uuid

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=10.55)
    image = models.ImageField()
    ingredients_product = models.TextField(max_length=200)
    combo = models.BooleanField(default=False)
    description_product = models.TextField(max_length=1000)
    banner = models.ImageField(blank=True)
    banner_include = models.BooleanField(default=False)
    highlight_section_title = models.ImageField(blank=True)
    highlight_section_product = models.ImageField(blank=True)
    highlight_section_name = models.ImageField(blank=True)
    highlight_include = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    completed = models.BooleanField(default=False)

    @property
    def get_cart_total(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.get_total for item in cartitems])
        return total

    @property
    def get_itemtotal(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

    def __str__(self):
        return str(self.id)

class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def get_total(self):
        total = self.quantity * self.product.price
        if total == 0.00:
            self.delete()
        return total

    def __str__(self):
        return self.product.name

class ShippindAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.address

""" class BannerProduct(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.ImageField()

    def __str__(self):
        return self.title """

class Perfume_search(models.Model):
    name_of_perfume = models.CharField(max_length=100)
    def __str__(self):
        return self.name_of_perfume


class Location(models.Model):
    name_location = models.CharField(max_length=100, blank=True)
    map_location = models.TextField(max_length=500)
    def __str__(self):
        return self.name_location
    
