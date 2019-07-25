from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import User_Profile
from recipes.models import Recipes
from django.contrib.auth.models import User

@login_required
def user_profile(request):
    currentUser = request.user
    if request.user.username != 'admin':
        userProfile = User_Profile.objects.get(user = currentUser)
        user_recipes = Recipes.objects.filter(author = currentUser)
        context = {
            'userProfile':userProfile,
            'user_recipes':user_recipes,
        }
        return render(request,'user_profile/user_profile.html',context)
    else:
        return redirect('/accounts/logout/')
