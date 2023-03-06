from django.contrib import admin
from . models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'combo', 'banner_include', 'highlight_include')
    
    list_display_links = ('id','name', 'price')

    #list_filter = ('nome', 'sobrenome')

    list_per_page = 10

    search_fields = ('name', 'price')



""" class BannerProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image',)
    
    list_display_links = ('id','title',)

    #list_filter = ('nome', 'sobrenome')

    list_per_page = 10

    search_fields = ('title', 'description') """

admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(ShippindAddress)
""" admin.site.register(BannerProduct, BannerProductAdmin) """
admin.site.register(Perfume_search)
admin.site.register(Location)
