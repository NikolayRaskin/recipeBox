from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .regForm import RegForm

from django.contrib import messages


def mainPage(request):
    return render(request,'mainPage/mainPage.html')

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        user_name = 0
        user_email = 0
        user_pass = 0
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_pass = form.cleaned_data['password']
            user_pass_confirm = form.cleaned_data['confirm_password']
            
            if username_exists(user_name):
                messages.info(request, 'Логин занят!')
                return HttpResponseRedirect('/register/')
            elif email_exists(user_email):
                messages.info(request, 'Email занят!')
                return HttpResponseRedirect('/register/')
            elif user_pass != user_pass_confirm:
                messages.info(request, 'Заданный пароль и подтверждение пароля не совпадают!')
                return HttpResponseRedirect('/register/')
            else:
                user = User.objects.create_user(user_name, user_email, user_pass)
                login(request,user)
                return redirect('/')
    else:
        form = RegForm()
    return render(request,'registration/register.html',{'form':form})

def username_exists(user_name):
    if User.objects.filter(username=user_name).exists():
        return True
    else:
        return False
def email_exists(user_email):
    if User.objects.filter(email=user_email).exists():
        return True
    else:
        return False