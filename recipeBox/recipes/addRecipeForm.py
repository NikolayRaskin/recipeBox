from django import forms
KINDOFDISH = ( ('Закуска','Закуска'),
               ('Салат','Салат'),
               ('Суп','Суп'),
               ('Основное блюдо','Основное блюдо'),
               ('Напиток','Напиток'),
               ('Заготовка','Заготовка') )

CHOICESOFDISH = ( ('Мясное','Мясное'),
                  ('Рыбное','Рыбное'),
                  ('Вегетарианское','Вегетарианское') )

MEAT_CHOICES =  ( ('Курица','Курица'),
                  ('Говядина','Говядина'),
                  ('Свинина','Свинина'),
                  ('Баранина','Баранина'),
                  ('Телятина','Телятина'),
                  ('Черепаха','Черепаха') )

FISH_CHOICES =  ( ('Окунь','Окунь'),
                  ('Карп','Карп'),
                  ('Сибас','Сибас'),
                  ('Сёмга','Сёмга'),
                  ('Акула','Акула'),
                  ('Щука','Щука') )

CALCUNITOFINGREDIANTS = ( ('Грамм','Грамм'),
                          ('Штук','Штук'),
                          ('Ст. ложек','Ст. ложек'),
                          ('Чай. ложек','Чай. ложек'),
                          ('МГрамм','МГрамм'),
                          ('Литров','Литров'),
                          ('МЛитров','МЛитров') )

LEVEL = (
    ('Уровень 1', 'Уровень 1'),
    ('Уровень 2', 'Уровень 2'),
    ('Уровень 3', 'Уровень 3'),
)

COUNTRYS = [ ('Беларусь','Беларусь'),('Россия','Россия'),('США','США'),('Италия','Италия'),('Испания','Испания'),('Австралия','Австралия'),                ('Кубань','Кубань'),('Германия','Германия'),('Китай','Китай'),('Япония','Япония'),('Корея','Корея'),('Нидерланды','Нидерланды'),              ('Франция','Франция'),('Канада','Канада'),('Мексика','Мексика') ]

COUNTRYS.sort()
COUNTRYS = tuple(COUNTRYS)

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Название'}))
    
    country = forms.ChoiceField(widget=forms.Select,choices=COUNTRYS)
    
    kindOfDish = forms.ChoiceField(widget=forms.Select,choices=KINDOFDISH)
    
    typeOfDish = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICESOFDISH)
    kindOfMeat = forms.ChoiceField(widget=forms.Select,choices=MEAT_CHOICES,required=False,initial=None)
    kindOfFish = forms.ChoiceField(widget=forms.Select,choices=FISH_CHOICES,required=False,initial=None)
    #----------------------------------------------
    #----------------------------------------------
    
    #1----------------------------------------------
    nameOfIngrediants1 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ингредиент'}))
    countOfIngrediants1 = forms.IntegerField()
    calcUnitOfIngrediants1 = forms.ChoiceField(widget=forms.Select,choices=CALCUNITOFINGREDIANTS)
    #2----------------------------------------------
    nameOfIngrediants2 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ингредиент'}),required=False,initial=None)
    countOfIngrediants2 = forms.IntegerField(required=False,initial=None)
    calcUnitOfIngrediants2 = forms.ChoiceField(widget=forms.Select,choices=CALCUNITOFINGREDIANTS,required=False,initial=None)
    #3----------------------------------------------
    nameOfIngrediants3 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ингредиент'}),required=False,initial=None)
    countOfIngrediants3 = forms.IntegerField(required=False,initial=None)
    calcUnitOfIngrediants3 = forms.ChoiceField(widget=forms.Select,choices=CALCUNITOFINGREDIANTS,required=False,initial=None)
    #4----------------------------------------------
    nameOfIngrediants4 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ингредиент'}),required=False,initial=None)
    countOfIngrediants4 = forms.IntegerField(required=False,initial=None)
    calcUnitOfIngrediants4 = forms.ChoiceField(widget=forms.Select,choices=CALCUNITOFINGREDIANTS,required=False,initial=None)
    #5----------------------------------------------
    nameOfIngrediants5 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ингредиент'}),required=False,initial=None)
    countOfIngrediants5 = forms.IntegerField(required=False,initial=None)
    calcUnitOfIngrediants5 = forms.ChoiceField(widget=forms.Select,choices=CALCUNITOFINGREDIANTS,required=False,initial=None)
    #6----------------------------------------------
    nameOfIngrediants6 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ингредиент'}),required=False,initial=None)
    countOfIngrediants6 = forms.IntegerField(required=False,initial=None)
    calcUnitOfIngrediants6 = forms.ChoiceField(widget=forms.Select,choices=CALCUNITOFINGREDIANTS,required=False,initial=None)
    #7----------------------------------------------
    nameOfIngrediants7 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ингредиент'}),required=False,initial=None)
    countOfIngrediants7 = forms.IntegerField(required=False,initial=None)
    calcUnitOfIngrediants7 = forms.ChoiceField(widget=forms.Select,choices=CALCUNITOFINGREDIANTS,required=False,initial=None)
    #8----------------------------------------------
    nameOfIngrediants8 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ингредиент'}),required=False,initial=None)
    countOfIngrediants8 = forms.IntegerField(required=False,initial=None)
    calcUnitOfIngrediants8 = forms.ChoiceField(widget=forms.Select,choices=CALCUNITOFINGREDIANTS,required=False,initial=None)
    #9----------------------------------------------
    nameOfIngrediants9 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ингредиент'}),required=False,initial=None)
    countOfIngrediants9 = forms.IntegerField(required=False,initial=None)
    calcUnitOfIngrediants9 = forms.ChoiceField(widget=forms.Select,choices=CALCUNITOFINGREDIANTS,required=False,initial=None)
    #10---------------------------------------------
    nameOfIngrediants10 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ингредиент'}),required=False,initial=None)
    countOfIngrediants10 = forms.IntegerField(required=False,initial=None)
    calcUnitOfIngrediants10 = forms.ChoiceField(widget=forms.Select,choices=CALCUNITOFINGREDIANTS,required=False,initial=None)
    
    #----------------------------------------------
    #----------------------------------------------
    instruction = forms.CharField(max_length=5000, widget=forms.Textarea)
    description = forms.CharField(max_length=5000, widget=forms.Textarea,required=False)
    oursForCooking = forms.IntegerField(required=False)
    minutsForCooking = forms.IntegerField()
    level = forms.ChoiceField(widget=forms.Select,choices=LEVEL)
    
    
    
    