from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http.response import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login
from django.utils.safestring import mark_safe
from django.contrib import messages

def Homepage(request):
    return render(request, 'files/Homepage.html')

def Login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('AdminHomepage')
            elif user is not None and user.is_client:
                login(request, user)
                return redirect('Client')
            else:
                msg= 'Invalid Credentials'
        else:
            msg = 'Error Validating Form'
    return render(request, 'files/Login.html',{'form': form, 'msg': msg})

def Signup(request):
    msg = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User Created'
            return redirect('Login')
        else:
            error_text = '<ul style="display:flex;'\
              'flex-direction:column;list-style-type:none;"'
            for msg_list in form.errors.values():
                for msg in msg_list:
                    error_text += f'<li>{msg}</li>'
            error_text += '</ul>'
            messages.error(request, mark_safe(error_text))
    else:
        form = SignupForm()
    return render(request, 'files/Signup.html', {'form': form, 'msg': msg})

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

def TermsofPayment(request):
    return render(request, 'files/TermsofPayment.html')


