from django import forms

class RegForm(forms.Form):
    user_name = forms.CharField(label='Логин:', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Логин'}))    
    user_email = forms.EmailField(label='Email:',widget=forms.TextInput(attrs={'placeholder': 'Email'}))   
    password = forms.CharField(label='Пароль:',widget=forms.PasswordInput())