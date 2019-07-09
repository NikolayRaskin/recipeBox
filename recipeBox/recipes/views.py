from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .addRecipeForm import AddRecipeForm

@login_required
def addRecipe(request):
    form = AddRecipeForm()
    return render(request,'recipes/addRecipe.html',{'form':form})
