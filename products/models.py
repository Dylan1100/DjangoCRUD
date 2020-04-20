from django.db import models
from categories.models import Category

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    picture = models.ImageField()
