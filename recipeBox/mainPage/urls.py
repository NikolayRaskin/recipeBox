from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.mainPage, name = 'mainPage'),
    path('register/',views.register, name = 'register'),
]