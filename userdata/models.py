from django.db import models
from shop.models import Product  # Import ProductData from the correct path

class UserData(models.Model):
    user_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=15)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=25)
    user_cpassword = models.CharField(max_length=25)

    def __str__(self):
        return self.user_name

class Cart(models.Model):
    userdata = models.ForeignKey(UserData, on_delete=models.CASCADE)
    productdata = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.userdata.user_name}'s Cart"
