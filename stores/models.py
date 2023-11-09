from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.dispatch import receiver

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True, null=False, default=0.0)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='stores/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Store, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# signal to update slug automatically
@receiver(pre_save, sender=Store)
def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
