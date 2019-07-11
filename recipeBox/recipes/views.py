from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .addRecipeForm import AddRecipeForm
from .models import MeatDish,FishDish,VeganDish

@login_required
def addRecipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            ings = []
            
            title = form.cleaned_data['title']
            country = form.cleaned_data['country']
            kindOfDish = form.cleaned_data['kindOfDish']
            typeOfDish = form.cleaned_data['typeOfDish']
            kindOfMeat = form.cleaned_data['kindOfMeat']
            kindOfFish = form.cleaned_data['kindOfFish']
            
            #-----------------------------------
            names=[form.cleaned_data['nameOfIngrediants1'],form.cleaned_data['nameOfIngrediants2'],form.cleaned_data['nameOfIngrediants3'],form.cleaned_data['nameOfIngrediants4'],form.cleaned_data['nameOfIngrediants5'],form.cleaned_data['nameOfIngrediants6'],form.cleaned_data['nameOfIngrediants7'],form.cleaned_data['nameOfIngrediants8'],form.cleaned_data['nameOfIngrediants9'],form.cleaned_data['nameOfIngrediants10']]
            counts=[form.cleaned_data['countOfIngrediants1'],form.cleaned_data['countOfIngrediants2'],form.cleaned_data['countOfIngrediants3'],form.cleaned_data['countOfIngrediants4'],form.cleaned_data['countOfIngrediants5'],form.cleaned_data['countOfIngrediants6'],form.cleaned_data['countOfIngrediants7'],form.cleaned_data['countOfIngrediants8'],form.cleaned_data['countOfIngrediants9'],form.cleaned_data['countOfIngrediants10']]
            calcs=[form.cleaned_data['calcUnitOfIngrediants1'],form.cleaned_data['calcUnitOfIngrediants2'],form.cleaned_data['calcUnitOfIngrediants3'],form.cleaned_data['calcUnitOfIngrediants4'],form.cleaned_data['calcUnitOfIngrediants5'],form.cleaned_data['calcUnitOfIngrediants6'],form.cleaned_data['calcUnitOfIngrediants7'],form.cleaned_data['calcUnitOfIngrediants8'],form.cleaned_data['calcUnitOfIngrediants9'],form.cleaned_data['calcUnitOfIngrediants10']]
            #-----------------------------------
            
            instruction = form.cleaned_data['instruction']
            description = form.cleaned_data['description']
            oursForCooking = form.cleaned_data['oursForCooking']
            minutsForCooking = form.cleaned_data['minutsForCooking']
            level = form.cleaned_data['level']
            
            for i in range(len(names)):
                ings.append({str(i) + '. ' + str(names[i]):str(counts[i]) + ' ' + calcs[i]})
            
            if typeOfDish == 'Мясное':
                new_recipe = MeatDish()
                new_recipe.kindOfMeat = kindOfMeat
            elif typeOfDish == 'Рыбное':
                new_recipe = FishDish()
                new_recipe.kindOfFish = kindOfFish
            elif typeOfDish == 'Вегетарианское':
                new_recipe = VeganDish()
                
            new_recipe.author = request.user
            new_recipe.title = title
            new_recipe.country = country
            new_recipe.kindOfDish = kindOfDish
            new_recipe.ingredients = ings
            new_recipe.instruction = instruction
            new_recipe.description = description
            new_recipe.oursForCooking = oursForCooking
            new_recipe.minutsForCooking = minutsForCooking
            new_recipe.level = level
            new_recipe.save()
            
            
            
            return redirect('/user_profile/')
        else:
            print('not valid')
    else:
        form = AddRecipeForm()
    return render(request,'recipes/addRecipe.html',{'form':form})
