# userdata/admin.py
from django.contrib import admin
from .models import UserData, Cart

class CartInline(admin.TabularInline):
    model = Cart
    extra = 1

class UserDataAdmin(admin.ModelAdmin):
    inlines = [CartInline]
    list_display = ('user_name', 'user_phone', 'user_email', 'user_password', 'user_cpassword')

class CartAdmin(admin.ModelAdmin):
    list_display = ('userdata', 'productdata', 'quantity')

admin.site.register(UserData, UserDataAdmin)
admin.site.register(Cart, CartAdmin)
