from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password2")

class SignupForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField
    username = forms.CharField(label="username")
    email = forms.CharField(label="email")
    password1 = forms.CharField()
    password2 = forms.CharField(label="password2")

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2','is_admin','is_client')