from django import forms
KINDOFDISH=(('Закуска'),
            ('Салат'),
            ('Суп'),
            ('Основное блюдо'),
            ('Напиток'))
CHOICESOFDISH=(('Мясное','Мясное'),
               ('Рыбное','Рыбное'),
               ('Вегетарианское','Вегетарианское'))
MEAT_CHOICES =  (
                ('Курица','Курица'),
                ('Говядина','Говядина'),
                ('Свинина','Свинина'),
                ('Баранина','Баранина'),
                ('Телятина','Телятина'),
                ('Черепаха','Черепаха'))

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Название'}))
    typeOfDish = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICESOFDISH)
    kindOfMeat = forms.ChoiceField(widget=forms.Select,choices=MEAT_CHOICES)
    kindOfFish = forms.CharField(max_length=100)
    
    
    