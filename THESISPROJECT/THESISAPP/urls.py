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
    path('AdminHomepage/<int:pk>', views.AdminHomepage, name='AdminHomepage'),
    path('Application/<int:pk>/<str:email>', views.Application, name='Application'),
    path('ApplicationApprove/<int:pk>/<str:email>', views.ApplicationApprove, name='ApplicationApprove'),
    path('ApplicationReject/<int:pk>/<str:email>', views.ApplicationReject, name='ApplicationReject'),
    path('Appointment/<int:pk>/<str:email>', views.Appointment, name='Appointment'),
    path('AppointmentApprove/<int:pk>/<str:email>', views.AppointmentApprove, name='AppointmentApprove'),
    path('AppointmentReject/<int:pk>/<str:email>', views.AppointmentReject, name='AppointmentReject'),
    path('BuyersApplication/<int:pk>/<str:email>', views.BuyersApplication, name='BuyersApplication'), 
    path('BuyersApplicationApprove/<int:pk>/<str:email>', views.BuyersApplicationApprove, name='BuyersApplicationApprove'), 
    path('BuyersApplicationReject/<int:pk>/<str:email>', views.BuyersApplicationReject, name='BuyersApplicationReject'),  
    path('ClientPayment/<int:pk>', views.ClientPayment, name='ClientPayment'),
    path('Addnew/<int:pk>', views.AddNew, name='AddNew'),
    path('AddnewUpdate/<int:pk>', views.AddNewUpdate, name='AddNewUpdate'),
    path('AddnewDelete/<int:pk>', views.AddNewDelete, name='AddNewDelete'),
    path('Notice/<int:pk>', views.Notice, name='Notice'),
    path('Notifier', views.Notifier, name='Notifier'),
    path('Inquiry/<int:pk>/<str:email>', views.Inquiry, name='Inquiry'),
    path('InquiryReject/<int:pk>/<str:email>', views.InquiryReject, name='InquiryReject'),
    path('InquiryApprove/<int:pk>/<str:email>', views.InquiryApprove, name='InquiryApprove'),
    path('PropertyManagement/<int:pk>', views.PropertyManagement, name='PropertyManagement'),
    path('PropertyManagementUpdate/<int:pk>', views.PropertyManagementUpdate, name='PropertyManagementUpdate'),
    path('PropertyManagementDelete/<int:pk>', views.PropertyManagementDelete, name='PropertyManagementDelete'),
    #---------------END ADMIN SIDE
    #---------------CLIENT SIDE
    path('Client/<int:pk>', views.Client, name='Client'),
    path('InstallmentBill/<int:pk>', views.InstallmentBill, name='InstallmentBill'),
    path('PaymentHistory/<int:pk>', views.PaymentHistory, name='PaymentHistory'),
    path('BuyersForm/<int:pk>', views.BuyersForm, name='BuyersForm'),
    path('BillSummary/<str:pk>', views.BillSummary, name='BillSummary'),
    path('ApplicationForm/<int:pk>', views.ApplicationForm, name='ApplicationForm'),
    path('BookAppointment/<int:pk>', views.BookAppointment, name='BookAppointment'),
    path('Property/<int:pk>', views.Property, name='Property'),
    #---------------END CLIENT SIDE
    
]