from django.db import models
from stores.models import Store

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    name = models.CharField(max_length=120)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    stock = models.IntegerField()
    description = models.TextField()
    category = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=6, decimal_places=2)
