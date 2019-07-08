from django.contrib import admin
from recipes.models import Country,MeatDish,FishDish,VeganDish

# Register your models here.
admin.site.register(Country)
admin.site.register(MeatDish)
admin.site.register(FishDish)
admin.site.register(VeganDish)
