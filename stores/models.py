from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Store, self).save(*args, **kwargs)

    def __str__(self):
        return self.name