from django import forms

class PassChangeForm(forms.Form):  
    password = forms.CharField(label='Новый пароль:',widget=forms.PasswordInput())    
    confirm_password = forms.CharField(label='Подтвердите новый пароль:',widget=forms.PasswordInput())