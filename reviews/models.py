from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class ProductReview(models.Model):
    class Meta:
        unique_together = ('product', 'author')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=50)
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reviews/')