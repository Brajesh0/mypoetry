from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RagistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
        