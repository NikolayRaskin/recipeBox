from django import forms
KINDOFDISH = (('Закуска','Закуска'),
              ('Салат','Салат'),
              ('Суп','Суп'),
              ('Основное блюдо','Основное блюдо'),
              ('Напиток','Напиток'),
              ('Заготовка','Заготовка'))
CHOICESOFDISH = (('Мясное','Мясное'),
                 ('Рыбное','Рыбное'),
                 ('Вегетарианское','Вегетарианское'))
MEAT_CHOICES =  (('Курица','Курица'),
                 ('Говядина','Говядина'),
                 ('Свинина','Свинина'),
                 ('Баранина','Баранина'),
                 ('Телятина','Телятина'),
                 ('Черепаха','Черепаха'))

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Название'}))
    
    kindOfDish = forms.ChoiceField(widget=forms.Select,choices=KINDOFDISH)
    
    typeOfDish = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICESOFDISH)
    kindOfMeat = forms.ChoiceField(widget=forms.Select,choices=MEAT_CHOICES)
    kindOfFish = forms.CharField(max_length=100)
    nameOfIngrediants = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ингредиент'}))
    countOfIngrediants = forms.IntegerField()
    instruction = forms.CharField(max_length=5000, widget=forms.Textarea)
    description = forms.CharField(max_length=5000, widget=forms.Textarea)
    oursForCooking = forms.IntegerField()
    minutsForCooking = forms.IntegerField()
    
    
    
    