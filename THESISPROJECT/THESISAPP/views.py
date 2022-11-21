from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http.response import HttpResponse
from .filters import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
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
                return redirect(f'AdminHomepage/{user.username}')
            elif user is not None and user.is_client:
                login(request, user)
                return redirect(f'Client/{user.pk}')
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
            email = form.cleaned_data.get('email')
            pk = User.objects.filter(email=email).values_list('id', flat=True).first()
            print(pk)
            ApplicationFormModel.objects.create(id_id=pk)
            BuyersFormModel.objects.create(id_id=pk)
            BookAppointmentModel.objects.create(id_id=pk)
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
def Client(request,pk):
    if request.user.is_authenticated and request.user.is_client:
        print("Client Page")
        a = User.objects.get(pk=pk)
        orders = a.lotorder_set.exclude(balance=0)
    else:
        return redirect('Logout')
    return render(request, 'files/Client.html', {'a':a,'orders':orders})

@login_required(login_url='/accounts/login/')
def ApplicationForm(request, pk):
    if request.user.is_authenticated and request.user.is_client:
        print("Application Page")
        a = User.objects.filter(pk=pk)
        b = ApplicationFormModel.objects.get(id_id=pk)
        form = ApplicationFormForm(instance=b)
        if request.method == 'POST':
            form = ApplicationFormForm(request.POST, instance=b)
            if form.is_valid():
                form.save()
                print('success')
    else:
        return redirect('Logout')
    return render(request, 'files/ApplicationForm.html',{'a':a, 'form':form})

@login_required(login_url='/accounts/login/')
def BookAppointment(request,pk):
    if request.user.is_authenticated and request.user.is_client:
        print ("Success")
        a = User.objects.filter(pk=pk)
        b = BookAppointmentModel.objects.get(id_id=pk)
        form = BookAppointmentForm(instance=b)
        if request.method == 'POST':
            form = BookAppointmentForm(request.POST, instance=b)
            if form.is_valid():
                form.save()
                print('success')
    else:
        return redirect('Logout')
    return render(request, 'files/BookAppointment.html',{'a':a, 'form':form})
    
@login_required(login_url='/accounts/login/')
def BuyersForm(request, pk):
    if request.user.is_authenticated and request.user.is_client:
        print ("Buyers Form Page")
        a = User.objects.filter(pk=pk)
        b = BuyersFormModel.objects.get(id_id=pk)
        form = BuyersFormForm(instance=b)
        if request.method == 'POST':
            form = BuyersFormForm(request.POST, instance=b)
            if form.is_valid():
                form.save()
                print('Success')
    else:
        return redirect('Logout')
    return render(request, 'files/BuyersForm.html', {'a':a, 'form':form})

@login_required(login_url='/accounts/login/')
def BillSummary(request, pk):
    if request.user.is_authenticated and request.user.is_client:
        print ("Bill Summary Page")
        a = User.objects.get(id=pk)
        orders = a.lotorder_set.all()
    else:
        return redirect('Logout')
    return render(request, 'files/BillSummary.html',{'a':a,'orders':orders})

@login_required(login_url='/accounts/login/')
def InstallmentBill(request, pk):
    if request.user.is_authenticated and request.user.is_client:
        print ("Success")
        a = User.objects.filter(pk=pk)
    else:
        return redirect('Logout')
    return render(request, 'files/InstallmentBill.html',{'a':a})

@login_required(login_url='/accounts/login/')
def PaymentHistory(request, pk):
    if request.user.is_authenticated and request.user.is_client:
        print ("Success")
        a = User.objects.filter(pk=pk)
    else:
        return redirect('Logout')
    return render(request, 'files/PaymentHistory.html', {'a':a})

@login_required(login_url='/accounts/login/')
def Property(request, pk):
    if request.user.is_authenticated and request.user.is_client:
        print ("Success")
        a = User.objects.filter(pk=pk)
    else:
        return redirect('Logout')
    return render(request, 'files/Property.html',{'a':a})
# ---------- END CLIENT

# ---------- ADMIN
@login_required(login_url='/accounts/login/')
def AdminHomepage(request, username):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Admin Homepage")
        a = User.objects.filter(username=username)
    else:
        return redirect('Logout')
    return render(request, 'files/AdminHomepage.html', {'a':a})

@login_required(login_url='/accounts/login/')
def ClientPayment(request, pk):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Client Payment Page")
        a = User.objects.get(id=pk)
        orders = LotOrder.objects.order_by('due_date')
        myFilter = clientpaymentFilter(request.GET, queryset=orders)
        orders = myFilter.qs
    else:
        return redirect('Logout')
    return render(request, 'files/ClientPayment.html',{'a':a,'orders':orders,'myFilter':myFilter})

@login_required(login_url='/accounts/login/')
def PropertyManagement(request, pk):
    if request.user.is_authenticated and request.user.is_admin:
        print ("PropertyManagement Page")
        a = User.objects.filter(pk=pk)
        form = LotOrderForm
        if request.method == 'POST':
            form = LotOrderForm(request.POST)
            if form.is_valid():
                form.save()
    else:
        return redirect('Logout')
    return render(request, 'files/PropertyManagement.html',{'a':a, 'form':form})

@login_required(login_url='/accounts/login/')
def PropertyManagementUpdate(request, pk):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        order = LotOrder.objects.get(id=pk)
        form = LotOrderForm(instance=order)
        if request.method == 'POST':
            form = LotOrderForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
    return render(request, 'files/PropertyManagement.html',{'a':a, 'form':form,'order':order})

@login_required(login_url='/accounts/login/')
def Notifier(request):
    if request.user.is_authenticated and request.user.is_admin:
        form = NotifierForm()
        if request.method == 'POST':
            form = NotifierForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                name = form.cleaned_data.get('name')
                totalamountdue = form.cleaned_data.get('totalamountdue')
                duedate = form.cleaned_data.get('duedate')
                send_mail(
                'Himlayang Cemetery Billing', 
                f'Good day {name}, \n \n You need to pay your monthy fee. Your due date is {duedate} with a total balance of {totalamountdue}. Thank you! \n\n Himlayang Cemetery Marketing Department \n' ,
                'andrewleilaraqueljustin@gmail.com',
                [email],
                fail_silently=False
            )
                print(email,name,totalamountdue,duedate)
            else:
                print("ERROR")
    else:
        return redirect('Logout')
    return render(request, 'files/Notifier.html',{'form':form})

@login_required(login_url='/accounts/login/')
def PropertyManagementDelete(request,pk):
    if request.user.is_authenticated and request.user.is_admin:
        b = LotOrder.objects.filter(id=pk).delete()
        orders = LotOrder.objects.all()
    
    return render(request, 'files/ClientPayment.html',{'b':b,'orders':orders})
@login_required(login_url='/accounts/login/')
def AddNew(request, pk):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Adding Lots Page")
        a = User.objects.filter(pk=pk)
    else:
        return redirect('Logout')
    return render(request, 'files/AddNew.html',{'a':a})

@login_required(login_url='/accounts/login/')
def BuyersApplication(request, pk, email):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Buyers Application Page")
        a = User.objects.filter(pk=pk)
        buyers_table = BuyersFormModel.objects.exclude(fullname=None)
        myFilter = buyersFilter(request.GET, queryset=buyers_table)
        buyers_table = myFilter.qs
        
    else:
        return redirect('Logout')
    return render(request, 'files/BuyersApplication.html',{'a':a, 'buyers_table':buyers_table, 'myFilter': myFilter})

@login_required(login_url='/accounts/login/')
def BuyersApplicationApprove(request, pk, email):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = BuyersFormModel.objects.filter(email=email).values_list('email', flat=True).first()
        send_mail(
                'Himlayang Cemetery',
                'Your application is Approve. You may come to the Municipal of General Trias. Thank you',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        BuyersFormModel.objects.filter(pk=pk).update(
            lot_type=None,phase=None,block=None,terms=None,fullname=None,age=None,gender=None,contacts=None,address=None,email=None)
        return redirect('BuyersApplication', pk=c, email=email)
    else:
        print('error')

@login_required(login_url='/accounts/login/')
def BuyersApplicationReject(request, pk, email):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = BuyersFormModel.objects.filter(email=email).values_list('email', flat=True).first()
        send_mail(
                'Himlayang Cemetery',
                'Your application is Reject. Please try another slots. Thank you',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        BuyersFormModel.objects.filter(pk=pk).update(
            lot_type=None,phase=None,block=None,terms=None,fullname=None,age=None,gender=None,contacts=None,address=None,email=None)
        return redirect('BuyersApplication', pk=c, email=email)
    else:
        print('error')

@login_required(login_url='/accounts/login/')
def Appointment(request, pk,email):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Appointment Page")
        a = User.objects.filter(pk=pk)
        appointment_table = BookAppointmentModel.objects.exclude(email=None)
        myFilter = appointmentFilter(request.GET, queryset=appointment_table)
        appointment_table = myFilter.qs
    else:
        return redirect('Logout')
    return render(request, 'files/Appointment.html',{'a':a, 'appointment_table':appointment_table, 'myFilter': myFilter})

@login_required(login_url='/accounts/login/')
def AppointmentApprove(request, pk, email):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = BookAppointmentModel.objects.filter(email=email).values_list('email', flat=True).first()
        send_mail(
                'Himlayang Cemetery - Appointment Approved',
                'Your Apointment is Approve. You may come to the Municipal of General Trias. Thank you',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        BookAppointmentModel.objects.filter(pk=pk).update(reason=None,fullname=None,contacts=None,email=None,date=None)
        return redirect('Appointment', pk=c, email=email)
    else:
        print('error')
 
@login_required(login_url='/accounts/login/')
def AppointmentReject(request,pk,email):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = BookAppointmentModel.objects.filter(email=email).values_list('email', flat=True).first()
        send_mail(
                'Himlayang Cemetery - Appointment Rejected',
                'Your Apointment is Reject, Please try another date. Thank you',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        BookAppointmentModel.objects.filter(pk=pk).update(reason=None,fullname=None,contacts=None,email=None,date=None)
        return redirect('Appointment', pk=c, email=email)
    else:
        print('error')

@login_required(login_url='/accounts/login/')
def Inquiry(request, pk, email):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        inq_table = inquire.objects.all()
        myFilter = inquiryFilter(request.GET, queryset=inq_table)
        inq_table = myFilter.qs
    else:
        return redirect('Logout')
    return render(request, 'files/Inquiry.html',{'inq_table': inq_table ,'a':a,'myFilter':myFilter})
@login_required(login_url='/accounts/login/')

def InquiryApprove(request, pk, email):
    if request.user.is_authenticated and request.user.is_admin:
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = InquiryFormModel.objects.filter(email=email).values_list('email', flat=True).first()
        send_mail(
                'Himlayang Cemetery - Lot Available',
                f'Dear Customer,\n \nThe lot you had inquire is Available. You may create an account and buy your chosen lot. Thank you\n \n Himlayang Cemetery Marketing Department ',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        InquiryFormModel.objects.filter(id=pk).delete()
        inq_table = inquire.objects.all()
        return render(request, 'files/Inquiry.html',{'inq_table': inq_table})
    else:
        print('error')

@login_required(login_url='/accounts/login/')
def InquiryReject(request, pk, email):
    if request.user.is_authenticated and request.user.is_admin:
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = InquiryFormModel.objects.filter(email=email).values_list('email', flat=True).first()
        send_mail(
                'Himlayang Cemetery - Lot Unavailable',
                f'Dear Customer,\n \nThe lot you had inquire is unavailable. Try to inquire other lots. Thank you\n \n Himlayang Cemetery Marketing Department ',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        InquiryFormModel.objects.filter(id=pk).delete()
        inq_table = inquire.objects.all()
        return render(request, 'files/Inquiry.html',{'inq_table': inq_table})
    else:
        print('error')

@login_required(login_url='/accounts/login/')
def Application(request,pk,email):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Application Page")
        a = User.objects.filter(pk=pk)
        applicants_table = ApplicationFormModel.objects.exclude(fullname=None)
    else:
        return redirect('Logout')
    return render(request, 'files/Application.html',{'a':a, 'applicants_table':applicants_table})

@login_required(login_url='/accounts/login/')
def ApplicationApprove(request,pk,email):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = ApplicationFormModel.objects.filter(email=email).values_list('email', flat=True).first()
        send_mail(
                'Himlayang Cemetery - Application of Appartments Approved',
                'Your Application is Approve. You may come to the Municipal of General Trias. Thank you',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        ApplicationFormModel.objects.filter(pk=pk).update(
            date=None,phase=None,block=None,lotno=None,fullname=None,age=None,gender=None,contacts=None,address=None,email=None)
        return redirect('Application', pk=c, email=email)
    else:
        print('error')

@login_required(login_url='/accounts/login/')
def ApplicationReject(request,pk,email):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = ApplicationFormModel.objects.filter(email=email).values_list('email', flat=True).first()
        send_mail(
                'Himlayang Cemetery - Application of Appartments Rejected',
                'Your Application is Reject. Try another slots. Thank you',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        ApplicationFormModel.objects.filter(pk=pk).update(
            date=None,phase=None,block=None,lotno=None,fullname=None,age=None,gender=None,contacts=None,address=None,email=None)
        return redirect('Application', pk=c, email=email)
    else:
        print('error')

@login_required(login_url='/accounts/login/')
def Notice(request, pk):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
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
            else:
                print("ERROR")
    else:
        return redirect('Logout')
    return render(request, 'files/Notice.html', {'form':form, 'a':a})

# ---------- END ADMIN

# ---------- NO LOGIN
def Niche(request):
    return render(request, 'files/Niche.html')

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