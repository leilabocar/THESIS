from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_client = models.BooleanField('Is client', default=False)

class InquiryForm(models.Model):
    lot_type = models.CharField(max_length=30, verbose_name='lot_type')
    phase = models.CharField(max_length=30, verbose_name='phase')
    block = models.CharField(max_length=30, verbose_name='block')
    lotno = models.CharField(max_length=30, verbose_name='lot_no.')
    terms = models.CharField(max_length=30, verbose_name='termsofpayment')
    fullname = models.CharField(max_length=99, verbose_name='fullname')
    age = models.IntegerField(verbose_name='age')
    gender = models.CharField(max_length=30, verbose_name='gender')
    contacts = models.IntegerField(verbose_name='contacts')
    address = models.CharField(max_length=30, verbose_name='address')
    email = models.EmailField(max_length=99, verbose_name='email')


    