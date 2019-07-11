from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .addRecipeForm import AddRecipeForm

@login_required
def addRecipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            kindOfDish = form.cleaned_data['kindOfDish']
            typeOfDish = form.cleaned_data['typeOfDish']
            kindOfMeat = form.cleaned_data['kindOfMeat']
            kindOfFish = form.cleaned_data['kindOfFish']
            nameOfIngrediants = form.cleaned_data['nameOfIngrediants']
            countOfIngrediants = form.cleaned_data['countOfIngrediants']
            instruction = form.cleaned_data['instruction']
            description = form.cleaned_data['description']
            oursForCooking = form.cleaned_data['oursForCooking']
            minutsForCooking = form.cleaned_data['minutsForCooking']
            print(title)
            print(kindOfDish)
            print(typeOfDish)
            print(kindOfMeat)
            print(kindOfFish)
            print(nameOfIngrediants)
            print(countOfIngrediants)
            print(instruction)
            print(description)
            print(oursForCooking)
            print(minutsForCooking)
            return redirect('/user_profile/')
        else:
            print('not valid')
    else:
        form = AddRecipeForm()
    return render(request,'recipes/addRecipe.html',{'form':form})
