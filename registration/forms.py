from django import forms

from django.contrib.auth.models import User

class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        model = User
        fields = ('username','email','password')
        labels = {'username':"ユーザーID",'email':"メール"}

class LoginForm(forms.Form):
    name = forms.CharField(label='ユーザ名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="パスワード")