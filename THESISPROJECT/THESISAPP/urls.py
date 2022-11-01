from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('AdminHomepage', views.AdminHomepage, name='AdminHomepage'),
    path('Apartment', views.Apartment, name='Apartment'),
    path('Application', views.Application, name='Application'),
    path('Appointment', views.Appointment, name='Appointment'),
    path('BuyersApplication', views.BuyersApplication, name='BuyersApplication'),  
    path('ClientPayment', views.ClientPayment, name='ClientPayment'),
    path('GraveFinder', views.GraveFinder, name='GraveFinder'),
    path('Inquiry', views.Inquiry, name='Inquiry'),
    path('InquiryForm', views.InquiryForm, name='InquiryForm'),
    #---------------CLIENT SIDE
    path('Client/<str:username>', views.Client, name='Client'),
    path('InstallmentBill/<int:pk>', views.InstallmentBill, name='InstallmentBill'),
    path('PaymentHistory/<int:pk>', views.PaymentHistory, name='PaymentHistory'),
    path('BuyersForm/<int:pk>', views.BuyersForm, name='BuyersForm'),
    path('BillSummary/<int:pk>', views.BillSummary, name='BillSummary'),
    path('ApplicationForm/<int:pk>', views.ApplicationForm, name='ApplicationForm'),
    path('BookAppointment/<int:pk>', views.BookAppointment, name='BookAppointment'),
     path('Property/<int:pk>', views.Property, name='Property'),
    #---------------END CLIENT SIDE
    path('Lawn', views.Lawn, name='Lawn'),
    path('Login', views.Login, name='Login'),
    path('Mausoleum', views.Mausoleum, name='Mausoleum'),
    path('Niche', views.Niche, name='Niche'),
    path('Notice', views.Notice, name='Notice'),
    path('Notifier', views.Notifier, name='Notifier'),
    path('Signup', views.Signup, name='Signup'),
    path('TermsofPayment', views.TermsofPayment, name='TermsofPayment'),
    path('Logout', views.Logout, name='Logout'),
    path('accounts/login/', views.Logout),
]