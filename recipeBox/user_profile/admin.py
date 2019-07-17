from django.contrib import admin
from .models import FavoriteItem,User_Profile

# Register your models here.
admin.site.register(FavoriteItem)
admin.site.register(User_Profile)
