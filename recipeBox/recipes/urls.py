from django.urls import path,include
from . import views

urlpatterns = [
    path('addRecipe/',views.addRecipe, name = 'addRecipe'),
]