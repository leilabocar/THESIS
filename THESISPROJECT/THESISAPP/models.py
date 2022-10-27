from email.policy import default
from random import choices
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_client = models.BooleanField('Is client', default=False)

class InquiryForm(models.Model):
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

    lot_type = models.CharField(max_length=30, choices=lot_type_choices, verbose_name='lot_type')
    phase = models.CharField(max_length=30, verbose_name='phase')
    block = models.CharField(max_length=30, verbose_name='block')
    lotno = models.CharField(max_length=30, verbose_name='lot_no.')
    terms = models.CharField(max_length=30, choices=terms_choices, verbose_name='termsofpayment')
    fullname = models.CharField(max_length=99, verbose_name='fullname')
    age = models.IntegerField(verbose_name='age')
    gender = models.CharField(max_length=30, verbose_name='gender')
    contacts = models.CharField(max_length=11, verbose_name='contacts')
    address = models.CharField(max_length=99, verbose_name='address')
    email = models.EmailField(max_length=99, verbose_name='email')


    