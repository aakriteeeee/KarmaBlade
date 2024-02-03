from django.contrib import admin 

from shop.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','product_detail','product_price','product_image')

# Register your models here.

admin.site.register(Product, ProductAdmin)
