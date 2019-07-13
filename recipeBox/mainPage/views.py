from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .regForm import RegForm
from .email_passResetForm import EmailPassResetForm
from .passChangeForm import PassChangeForm
from recipes.models import MeatDish,FishDish,VeganDish

from django.contrib import messages

import re

def mainPage(request):
    easy_to_cook = []
    if MeatDish.objects.filter(level='Уровень 1'):
        easy_to_cook.append(MeatDish.objects.filter(level='Уровень 1'))
    if FishDish.objects.filter(level='Уровень 1'):
        easy_to_cook.append(FishDish.objects.filter(level='Уровень 1'))
    if VeganDish.objects.filter(level='Уровень 1'):
        easy_to_cook.append(VeganDish.objects.filter(level='Уровень 1'))
    context = {
        'easy_to_cook':easy_to_cook,
    }
    print('easy_to_cook:')
    for i in range(len(easy_to_cook)):
        for j in range(len(easy_to_cook[i])):
            print(type(easy_to_cook[i][j].ingredients))
            #print(easy_to_cook[i][j].title + '\nIngreditnts ' +  + '\n' )
    #print(easy_to_cook)
    return render(request,'mainPage/mainPage.html',context)

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_pass = form.cleaned_data['password']
            user_pass_confirm = form.cleaned_data['confirm_password']
            
            if username_exists(user_name):
                messages.info(request, 'Логин занят!')
                return render(request,'registration/register.html',{'form':form})
            elif email_exists(user_email):
                messages.info(request, 'Email занят!')
                return render(request,'registration/register.html',{'form':form})
            elif user_pass != user_pass_confirm:
                messages.info(request, 'Заданный пароль и подтверждение пароля не совпадают!')
                return render(request,'registration/register.html',{'form':form})
            else:
                if len(user_pass) < 8:
                    messages.info(request, 'Пароль должен содержать не меньше 8 символов!')
                    return render(request,'registration/register.html',{'form':form})
                elif re.search('[0-9]',user_pass) is None:
                    messages.info(request, 'Пароль должен содержать хотя бы одну цифру!')
                    return render(request,'registration/register.html',{'form':form})
                elif re.search('[A-Z]',user_pass) is None:
                    messages.info(request, 'Пароль должен содержать хотя бы одну заглавную букву!')
                    return render(request,'registration/register.html',{'form':form})
                else:
                    user = User.objects.create_user(user_name, user_email, user_pass)
                    login(request,user)
                    return redirect('/user_profile/')
    else:
        form = RegForm()
    return render(request,'registration/register.html',{'form':form})

def forgot_password(request):
    if request.method == 'POST':
        form = EmailPassResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if email_exists(email):
                send_email_for_reset_pass(email)
                return render(request,'registration/password_reset_sendEmail_done.html')
            else:
                messages.info(request, 'Данного email нет в базе!')
                #return HttpResponseRedirect('/forgot_password/')
                return render(request,'registration/password_reset_form.html',{'form':form})
    else:
        form = EmailPassResetForm()
    return render(request,'registration/password_reset_form.html',{'form':form})

def reset_password(request,user_name):
    user = User.objects.get(username=user_name)
    if request.method == 'POST':
        form = PassChangeForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                messages.info(request, 'Заданный пароль и подтверждение пароля не совпадают!')
                return HttpResponseRedirect('/reset_password/'+user_name)
            else:
                if len(password) < 8:
                    messages.info(request, 'Пароль должен содержать не меньше 8 символов!')
                    return HttpResponseRedirect('/reset_password/'+user_name)
                elif re.search('[0-9]',password) is None:
                    messages.info(request, 'Пароль должен содержать хотя бы одну цифру!')
                    return HttpResponseRedirect('/reset_password/'+user_name)
                elif re.search('[A-Z]',password) is None:
                    messages.info(request, 'Пароль должен содержать хотя бы одну заглавную букву!')
                    return HttpResponseRedirect('/reset_password/'+user_name)
                else:
                    user.set_password(password)
                    user.save()
                    return render(request,'registration/pass_change_done.html')
    else:
        form = PassChangeForm()
    return render(request,'registration/pass_change.html',{'form':form,'user_name':str(user_name)})
        
        
        
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
    
def send_email_for_reset_pass(user_email):
    user = User.objects.filter(email=user_email)[0].get_username()
    subject = 'Запрос на сброс пароля пользователя: '+user+'.'
    message = "Вы получили это e-mail, потому что вы отправили запрос на сброс пароля для вашего аккаунта на Recipe Box.\n\nПожалуйста передите по указанной ниже ссылке и выберите новый пароль:\n\nhttp://127.0.0.1:8000/reset_password/"+ user +"\n\nСпасибо, что используете наш сайт!\n\nThe Recipe Box team."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail( subject, message, email_from, recipient_list )