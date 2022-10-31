from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http.response import HttpResponse
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
#EMAIL
from django.core.mail import EmailMultiAlternatives,send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
#MODELS
from .models import *
from .models import InquiryFormModel as inquire

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
                return redirect('Client', username==user.username)
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

# --------------- CLIENT
@login_required(login_url='/accounts/login/')
def Client(request,username):
    if request.user.is_authenticated and request.user.is_client:
        print ("Success")
    else:
        return redirect('Logout')
    return render(request, 'files/Client.html')

@login_required(login_url='/accounts/login/')
def ApplicationForm(request, id):
    if request.user.is_authenticated and request.user.is_client:
        applicant = ApplicationFormModel.objects.filter(id=id).first()
        if request.method == 'POST':
            form = ApplicationFormForm(request.POST or None, instance=applicant)
            if form.is_valid():
                form.save()
            else:
                print("Error")
        else:
            form = ApplicationFormForm(request.POST or None, instance=applicant)
    else:
        return redirect('Logout')
    return render(request, 'files/ApplicationForm.html',{'applicant':applicant,'form':form})

@login_required(login_url='/accounts/login/')
def BillSummary(request):
    if request.user.is_authenticated and request.user.is_client:
        print ("Success")
    else:
        return redirect('Logout')
    return render(request, 'files/BillSummary.html')

@login_required(login_url='/accounts/login/')
def BookAppointment(request):
    if request.user.is_authenticated and request.user.is_client:
        print ("Success")
    else:
        return redirect('Logout')
    return render(request, 'files/BookAppointment.html')

@login_required(login_url='/accounts/login/')
def InstallmentBill(request):
    if request.user.is_authenticated and request.user.is_client:
        print ("Success")
    else:
        return redirect('Logout')
    return render(request, 'files/InstallmentBill.html')

@login_required(login_url='/accounts/login/')
def BuyersForm(request):
    if request.user.is_authenticated and request.user.is_client:
        print ("Success")
    else:
        return redirect('Logout')
    return render(request, 'files/BuyersForm.html')

@login_required(login_url='/accounts/login/')
def PaymentHistory(request):
    if request.user.is_authenticated and request.user.is_client:
        print ("Success")
    else:
        return redirect('Logout')
    return render(request, 'files/PaymentHistory.html')

@login_required(login_url='/accounts/login/')
def Property(request):
    if request.user.is_authenticated and request.user.is_client:
        print ("Success")
    else:
        return redirect('Logout')
    return render(request, 'files/Property.html')
# ---------- END CLIENT

# ---------- ADMIN
@login_required(login_url='/accounts/login/')
def AdminHomepage(request):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Success")
    else:
        return redirect('Logout')
    return render(request, 'files/AdminHomepage.html')

@login_required(login_url='/accounts/login/')
def ClientPayment(request):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Success")
    else:
        return redirect('Logout')
    return render(request, 'files/ClientPayment.html')

@login_required(login_url='/accounts/login/')
def BuyersApplication(request):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Success")
    else:
        return redirect('Logout')
    return render(request, 'files/BuyersApplication.html')

@login_required(login_url='/accounts/login/')
def Appointment(request):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Success")
    else:
        return redirect('Logout')
    return render(request, 'files/Appointment.html')

@login_required(login_url='/accounts/login/')
def Inquiry(request):
    if request.user.is_authenticated and request.user.is_admin:
        inq_table = inquire.objects.all()
    else:
        return redirect('Logout')
    return render(request, 'files/Inquiry.html',{'inq_table': inq_table})

@login_required(login_url='/accounts/login/')
def Application(request):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Success")
    else:
        return redirect('Logout')
    return render(request, 'files/Application.html')

@login_required(login_url='/accounts/login/')
def Notice(request):
    if request.user.is_authenticated and request.user.is_admin:
        form = NoticeForm()
        if request.method == 'POST':
            form = NoticeForm(request.POST)
            if form.is_valid():
                receiver = form.cleaned_data.get('receiver')
                content = form.cleaned_data.get('content')
                send_mail(
                'Himlayang Cemetery',
                content,
                'andrewleilaraqueljustin@gmail.com',
                [receiver],
                fail_silently=False,
            )
                print("SUCCESS")
                return redirect('Notice')
            else:
                print("ERROR")
                return redirect('Notice')
    else:
        return redirect('Logout')
    return render(request, 'files/Notice.html', {'form':form})

# ---------- END ADMIN

# ---------- NO LOGIN
def Niche(request):
    return render(request, 'files/Niche.html')

def Notifier(request):
    return render(request, 'files/Notifier.html')

def TermsofPayment(request):
    return render(request, 'files/TermsofPayment.html')

def GraveFinder(request):
    return render(request, 'files/GraveFinder.html')

def InquiryForm(request):
    form = InquiryFormForm()
    if request.method == 'POST':
        form = InquiryFormForm(request.POST)
        if form.is_valid():
            form.save()
            print('Success')
            return redirect('InquiryForm')
        else:
            print('Error')
            return redirect('InquiryForm')
    return render(request, 'files/InquiryForm.html',{'form':form})

def Lawn(request):
    return render(request, 'files/Lawn.html')

def Mausoleum(request):
    return render(request, 'files/Mausoleum.html')

def Apartment(request):
    return render(request, 'files/Apartment.html')

def Logout(request):
    logout(request)
    return redirect ('Login')

# ---------- END NO LOGIN



