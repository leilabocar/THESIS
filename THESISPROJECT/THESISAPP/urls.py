from django.urls import path
from . import views


urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('AdminHomepage', views.AdminHomepage, name='AdminHomepage'),
    path('Apartment', views.Apartment, name='Apartment'),
    path('Application', views.Application, name='Application'),
    path('ApplicationForm', views.ApplicationForm, name='ApplicationForm'),
    path('Appointment', views.Appointment, name='Appointment'),
    path('BillSummary', views.BillSummary, name='BillSummary'),
    path('BookAppointment', views.BookAppointment, name='BookAppointment'),
    path('BuyersApplication', views.BuyersApplication, name='BuyersApplication'),
    path('BuyersForm', views.BuyersForm, name='BuyersForm'),
    path('Client', views.Client, name='Client'),
    path('ClientPayment', views.ClientPayment, name='ClientPayment'),
    path('GraveFinder', views.GraveFinder, name='GraveFinder'),
    path('Inquiry', views.Inquiry, name='Inquiry'),
    path('InquiryForm', views.InquiryForm, name='InquiryForm'),
    path('InstallmentBill', views.InstallmentBill, name='InstallmentBill'),
    path('Lawn', views.Lawn, name='Lawn'),
    path('Login', views.Login, name='Login'),
    path('Mausoleum', views.Mausoleum, name='Mausoleum'),
    path('Niche', views.Niche, name='Niche'),
    path('Notice', views.Notice, name='Notice'),
    path('Notifier', views.Notifier, name='Notifier'),
    path('PaymentHistory', views.PaymentHistory, name='PaymentHistory'),
    path('Property', views.Property, name='Property'),
    path('Signup', views.Signup, name='Signup'),
    path('TermsofPayment', views.TermsofPayment, name='TermsofPayment'),
]