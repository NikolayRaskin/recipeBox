from django import forms

COUNTRYS = [ ('Беларусь','Беларусь'),('Россия','Россия'),('США','США'),('Италия','Италия'),('Испания','Испания'),('Австралия','Австралия'),                ('Кубань','Кубань'),('Германия','Германия'),('Китай','Китай'),('Япония','Япония'),('Корея','Корея'),('Нидерланды','Нидерланды'),              ('Франция','Франция'),('Канада','Канада'),('Мексика','Мексика'),('Индия','Индия'),('Греция','Греция'),('Тайланд','Тайланд') ]
COUNTRYS.sort()
COUNTRYS = tuple(COUNTRYS)

class RegForm(forms.Form):
    user_name = forms.CharField(label='Логин:', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Логин'}))    
    user_email = forms.EmailField(label='Email:',widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    user_firstname = forms.CharField(label='Имя:', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Имя'})) 
    user_lastname = forms.CharField(label='Фамилия:', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    birth_date = forms.DateField()
    avatar = forms.ImageField(required=False)
    location = forms.ChoiceField(widget=forms.Select,choices=COUNTRYS)
    password = forms.CharField(label='Пароль:',widget=forms.PasswordInput())    
    confirm_password = forms.CharField(label='Подтвердите пароль:',widget=forms.PasswordInput())