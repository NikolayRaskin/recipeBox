from django.contrib import admin
from .models import MeatDish,FishDish,VeganDish

# Register your models here.
admin.site.register(MeatDish)
admin.site.register(FishDish)
admin.site.register(VeganDish)
