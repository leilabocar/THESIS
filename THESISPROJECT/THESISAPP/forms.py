from enum import unique
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

class InquiryFormForm(forms.ModelForm):
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

    lot_type = forms.ChoiceField(choices= lot_type_choices, widget=forms.RadioSelect, required=True)
    phase = forms.CharField()
    block = forms.CharField()
    lotno = forms.CharField()
    terms = forms.ChoiceField(choices= terms_choices, widget=forms.RadioSelect, required=True)
    fullname = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField()
    contacts = forms.CharField()
    address = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = InquiryFormModel
        fields = ('lot_type','phase','block','lotno','terms','fullname','age','gender','contacts','address','email')

        def contacts(self):
            n = self.cleaned_data.get('contacts')
            allowed_characters = '0123456789'
            for char in n:
                if char not in allowed_characters:
                    raise forms.ValidationError("Please only use numbers")
            return n

class NoticeForm(forms.Form):
    client = forms.CharField()
    receiver = forms.CharField()
    content = forms.CharField()

class ApplicationFormForm(forms.ModelForm):
    pk = forms.IntegerField()
    date = forms.DateField()
    phase = forms.CharField()
    block = forms.CharField()
    lotno = forms.CharField()
    fullname = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField()
    contacts = forms.CharField()
    address = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = ApplicationFormModel
        fields = ('date','phase','block','lotno','fullname','age','gender','contacts','address','email')


class BuyersFormForm(forms.ModelForm):
    lot_type_choices=[('Lawn Lot','Lawn Lot'),
                      ('Mausoleum','Mausoleum'),
                      ('Niche','Niche'),]
    
    terms_choices=[('Cash','Cash'),
                   ('1 Year','1 Year'),
                   ('2 Years','2 Years'),
                   ('3 Years','3 Years'),
                   ('Full Down','Full Down'),
                   ('Reservation','Reservation')]

    pk = forms.IntegerField()
    lot_type = forms.ChoiceField(choices= lot_type_choices, widget=forms.RadioSelect, required=True)
    phase = forms.CharField()
    block = forms.CharField()
    lotno = forms.CharField()
    terms = forms.ChoiceField(choices= terms_choices, widget=forms.RadioSelect, required=True)
    fullname = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField()
    contacts = forms.CharField()
    address = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = BuyersFormModel
        fields = ('lot_type','phase','block','lotno','terms','fullname','age','gender','contacts','address','email')

        def contacts(self):
            n = self.cleaned_data.get('contacts')
            allowed_characters = '0123456789'
            for char in n:
                if char not in allowed_characters:
                    raise forms.ValidationError("Please only use numbers")
            return n