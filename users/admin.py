from django.contrib import admin
from .models import WishList, UserProfile
# Register your models here.
admin.site.register(WishList)
admin.site.register(UserProfile)