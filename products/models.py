from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.text import slugify

from stores.models import Store

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20) 
    description = models.TextField()
    slug = models.SlugField(max_length=120, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#signal to edit category slug automatically
@receiver(pre_save, sender=Category)
def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


class Product(models.Model):
    name = models.CharField(max_length=120)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    stock = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    slug = models.SlugField(max_length=120, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#signal to edit product slug automatically
@receiver(pre_save, sender=Product)
def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


class Wishlist(models.Model):
    class Meta:
        unique_together = ('user', 'product')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' - ' + self.product.name