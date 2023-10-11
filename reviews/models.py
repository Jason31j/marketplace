from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from django.contrib.auth.models import User
from products.models import Product


def validate_rating(value):
    """
    Validates that the rating is between 0 and 5.

    Args:
        value (int): The rating value to validate.

    Raises:
        ValidationError: If the rating is not between 0 and 5.
    """
    if value < 0 or value > 5:
        raise ValidationError('The rating must be between 0 and 5')
class Review(models.Model):
    class Meta:
        unique_together = ('product', 'author')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    rating = models.IntegerField(validators=[validate_rating])

    def __str__(self):
        return self.tittle