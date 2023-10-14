from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 270px; margin: 0 auto;'}),label="ユーザ名")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'width: 270px; margin: 0 auto;'}),label="パスワード")
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control','style': 'width: 270px; margin: 0 auto;'}))

    class Meta():
        model = User
        fields = ('username','email','password')
        labels = {'username':"ユーザーID",'email':"メール"}

class LoginForm(forms.Form):
    name = forms.CharField(label='ユーザ名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="パスワード")

class DeleteForm(forms.Form):
    name = forms.CharField(label='ユーザ名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="パスワード")