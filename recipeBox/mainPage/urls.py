from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.mainPage, name = 'mainPage'),
    path('register/',views.register, name = 'register'),
    path('forgot_password/',views.forgot_password, name = 'forgot_password'),
    path('reset_password/<user_name>',views.reset_password, name = 'reset_password'),
]