from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('Apartment', views.Apartment, name='Apartment'),
    path('GraveFinder', views.GraveFinder, name='GraveFinder'),
    path('Lawn', views.Lawn, name='Lawn'),
    path('Login', views.Login, name='Login'),
    path('Mausoleum', views.Mausoleum, name='Mausoleum'),
    path('Niche', views.Niche, name='Niche'),
    path('Signup', views.Signup, name='Signup'),
    path('TermsofPayment', views.TermsofPayment, name='TermsofPayment'),
    path('Logout', views.Logout, name='Logout'),
    path('accounts/login/', views.Logout),
    path('InquiryForm', views.InquiryForm, name='InquiryForm'),
    #---------------ADMIN SIDE
    path('AdminHomepage/<str:username>', views.AdminHomepage, name='AdminHomepage'),
    path('Application/<int:pk>', views.Application, name='Application'),
    path('Appointment/<int:pk>', views.Appointment, name='Appointment'),
    path('AppointmentApprove/<int:pk>/<str:email>', views.AppointmentApprove, name='AppointmentApprove'),
    path('BuyersApplication/<int:pk>', views.BuyersApplication, name='BuyersApplication'),  
    path('ClientPayment/<int:pk>', views.ClientPayment, name='ClientPayment'),
    path('Notice/<int:pk>', views.Notice, name='Notice'),
    path('Notifier/<int:pk>', views.Notifier, name='Notifier'),
    path('Inquiry/<int:pk>', views.Inquiry, name='Inquiry'),
    #---------------END ADMIN SIDE
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
    
]