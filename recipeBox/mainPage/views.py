from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .regForm import RegForm

def mainPage(request):
    return render(request,'mainPage/mainPage.html')

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        user_name = 0
        user_email = 0
        user_pass = 0
        if form.is_valid():
            #form.save()
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_pass = form.cleaned_data['password']
            user = User.objects.create_user(user_name, user_email, user_pass)
            login(request,user)
            return redirect('/')
    else:
        form = RegForm()
    return render(request,'registration/register.html',{'form':form})