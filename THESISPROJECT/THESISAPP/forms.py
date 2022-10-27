from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password2")

class SignupForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField(label="Confirm Password")
    is_client = forms.BooleanField(initial=True, required=True)

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2','is_admin','is_client')

class InquiryFormForm(forms.Form):
    lot_type_choices=[('Lawn Lot','Lawn Lot'),
                      ('Mausoleum','Mausoleum'),
                      ('Niche','Niche'),
                      ('Apartment Type','Apartment Type')]
    
    terms_choices=[('Cash','Cash'),
                   ('1 Year','1 Year'),
                   ('2 Years','2 Years'),
                   ('3 Years','3 Years'),
                   ('Full Down','Full Down'),
                   ('Reservation','Reservation')]

    lot_type = forms.ChoiceField(choices=lot_type_choices, widget=forms.RadioSelect,initial=True, required=True)
    phase = forms.CharField()
    block = forms.CharField()
    lotno = forms.CharField()
    terms = forms.CharField(choices=terms_choices, widget=forms.RadioSelect, initial=True, required=True)
    fullname = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField()
    contacts = forms.IntegerField()
    address = forms.CharField()
    email = forms.EmailField()