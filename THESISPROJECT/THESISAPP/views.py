from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http.response import HttpResponse

def Homepage(request):
    return render(request, 'files/Homepage.html')

def AdminHomepage(request):
    return render(request, 'files/AdminHomepage.html')

def Apartment(request):
    return render(request, 'files/Apartment.html')

def Application(request):
    return render(request, 'files/Application.html')

def ApplicationForm(request):
    return render(request, 'files/ApplicationForm.html')

def Appointment(request):
    return render(request, 'files/Appointment.html')

def BillSummary(request):
    return render(request, 'files/BillSummary.html')

def BookAppointment(request):
    return render(request, 'files/BookAppointment.html')

def BuyersApplication(request):
    return render(request, 'files/BuyersApplication.html')

def BuyersForm(request):
    return render(request, 'files/BuyersForm.html')

def Client(request):
    return render(request, 'files/Client.html')

def ClientPayment(request):
    return render(request, 'files/ClientPayment.html')

def GraveFinder(request):
    return render(request, 'files/GraveFinder.html')

def Inquiry(request):
    return render(request, 'files/Inquiry.html')

def InquiryForm(request):
    return render(request, 'files/InquiryForm.html')

def InstallmentBill(request):
    return render(request, 'files/InstallmentBill.html')

def Lawn(request):
    return render(request, 'files/Lawn.html')

def Login(request):
    return render(request, 'files/Login.html')

def Mausoleum(request):
    return render(request, 'files/Mausoleum.html')

def Niche(request):
    return render(request, 'files/Niche.html')

def Notice(request):
    return render(request, 'files/Notice.html')

def Notifier(request):
    return render(request, 'files/Notifier.html')

def PaymentHistory(request):
    return render(request, 'files/PaymentHistory.html')

def Property(request):
    return render(request, 'files/Property.html')

def Signup(request):
    return render(request, 'files/Signup.html')

def TermsofPayment(request):
    return render(request, 'files/TermsofPayment.html')


