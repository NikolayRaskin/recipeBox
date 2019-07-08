from django import forms

class EmailPassResetForm(forms.Form):  
    email = forms.EmailField(label='Email:',widget=forms.TextInput(attrs={'placeholder': 'Email'}))