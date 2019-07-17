from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipes
from django.utils.translation import ugettext_lazy as _

class FavoriteItem(models.Model):
    recipe = models.ForeignKey('recipes.Recipes',on_delete=models.PROTECT)
    def __str__(self):
        return "Favorite recipe {0}".format(self.recipe.title)

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_firstname = models.CharField(max_length=100, blank=True)
    user_lastname = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='user_profile/static/user_profile/img/avatars/', null=True, blank=True)
    location = models.CharField(max_length=50, blank=True)
    date_joined = models.DateTimeField(_('Дата регистрации'), auto_now_add=True)
    birth_date = models.DateField(null=True, blank=True)
    favorites = models.ManyToManyField(FavoriteItem, blank = True, default=0)