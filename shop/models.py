from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=50 )
    product_detail=models.TextField()
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    product_image=models.ImageField(upload_to='product_images/')
