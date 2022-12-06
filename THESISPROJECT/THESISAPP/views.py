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
from django.core.paginator import Paginator

#EMAIL
from django.core.mail import EmailMultiAlternatives,send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
#MODELS
from .models import *
from .models import InquiryFormModel as inquire
from .models import PaymentHistory as PaymentHistory2
#paginator
from django.core.paginator import Paginator
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
                return redirect(f'AdminHomepage/{user.pk}')
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
        a = User.objects.get(pk=pk)
        history = a.paymenthistory_set.all()
    else:
        return redirect('Logout')
    return render(request, 'files/PaymentHistory.html', {'a':a,'history':history})

@login_required(login_url='/accounts/login/')
def Property(request, pk):
    if request.user.is_authenticated and request.user.is_client:
        a = User.objects.get(pk=pk)
        display = a.lotorder_set.filter(balance=0)
    else:
        return redirect('Logout')
    return render(request, 'files/Property.html',{'a':a,'display':display})
# ---------- END CLIENT

# ---------- ADMIN
@login_required(login_url='/accounts/login/')
def AdminHomepage(request, pk):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Admin Homepage")
        a = User.objects.filter(pk=pk)
        prod = Product.objects.order_by('-id')
        if 'name' in request.GET:
            q=request.GET['name']
            prod = Product.objects.filter(deceased__icontains=q)
        if 'lots' in request.GET:
            q=request.GET['lots']
            prod = Product.objects.filter(lot__icontains=q)
        else:
            pass
        p = Paginator(prod, per_page=10)
        page = request.GET.get('page')
        if page == None or page == "":
            page = "1"
        prods = p.get_page(page)
        prods.adjusted_elided_pages = p.get_elided_page_range(page)
    else:
        return redirect('Logout')
    return render(request, 'files/AdminHomepage.html', {'a':a,'prod':prod,'prods':prods})

@login_required(login_url='/accounts/login/')
def ClientPayment(request, pk):
    if request.user.is_authenticated and request.user.is_admin:
        q =''
        order = LotOrder.objects.order_by('-product')
        if 'name' in request.GET:
            q=request.GET['name']
            if q == '':
                order = LotOrder.objects.order_by('-product')
            else:
                order = LotOrder.objects.filter(customer_id__username__icontains=q)
        if 'lots' in request.GET:
            q=request.GET['lots']
            order = LotOrder.objects.filter(product_id__lot__icontains=q)
        else:
            pass
        p = Paginator(order, per_page=11)
        page = request.GET.get('page')
        if page == None or page == "":
            page = "1"
        orders = p.get_page(page)
        orders.adjusted_elided_pages = p.get_elided_page_range(page)
    else:
        return redirect('Logout')
    return render(request, 'files/ClientPayment.html',{'order':order,'orders':orders,'q':q})

@login_required(login_url='/accounts/login/')
def PropertyManagement(request, pk):
    if request.user.is_authenticated and request.user.is_admin:
        print ("PropertyManagement Page")
        a = User.objects.filter(pk=pk)
        form = LotOrderForm
        form1 = PaymentHistoryForm
        if request.method == 'POST':
            form = LotOrderForm(request.POST)
            form1 = PaymentHistoryForm(request.POST)
            if form.is_valid() and form1.is_valid():
                form.save()
                form1.save()
                messages.success(request, 'Successfully Added')
            else:
                messages.error(request, 'Invalid Input')
    else:
        return redirect('Logout')
    return render(request, 'files/PropertyManagement.html',{'a':a, 'form':form,'form1':form1})

@login_required(login_url='/accounts/login/')
def PropertyManagementUpdate(request, pk):
    if request.user.is_authenticated and request.user.is_admin:
        order = LotOrder.objects.get(id=pk)
        form = LotOrderForm(instance=order)
        form1 = PaymentHistoryForm()
        if request.method == 'POST':
            form = LotOrderForm(request.POST, instance=order)
            form1 = PaymentHistoryForm(request.POST)
            if form.is_valid() and form1.is_valid():
                form.save()
                form1.save()
                messages.success(request, 'Successfully Updated')
                return redirect('')
            else:
                messages.error(request, 'Invalid Input')
    else:
        return redirect('Logout')
    return render(request, 'files/PropertyManagement.html',{'form':form,'order':order, 'form1':form1})

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
        LotOrder.objects.filter(id=pk).delete()
        return redirect('ClientPayment',pk=pk)
    else:
        return redirect('Logout')
@login_required(login_url='/accounts/login/')
def AddNew(request, pk):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Adding Lots Page")
        a = User.objects.filter(pk=pk)
        form = ProductForm()
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully Added'),
                fail_silently=True
                return redirect('AddNew', pk=pk)
            else:
                messages.error(request,'Invalid Input')
    else:
        return redirect('Logout')
    return render(request, 'files/AddNew.html',{'a':a,'form':form})

@login_required(login_url='/accounts/login/')
def AddNewUpdate(request,pk):
    if request.user.is_authenticated and request.user.is_admin:
        prod= Product.objects.get(id=pk)
        form = ProductForm(instance=prod)
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=prod)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully Updated'),
                fail_silently=True
            else:
                messages.error(request, 'Invalid Input'),
                fail_silently=True
    else:
        return redirect('Logout')
    return render(request, 'files/AddNew.html',{'form':form,'prod':prod})

@login_required(login_url='/accounts/login/')
def AddNewDelete(request,pk):
    if request.user.is_authenticated and request.user.is_admin:
        Product.objects.filter(id=pk).delete()
        return redirect('AdminHomepage',pk=pk)
    else:
        return redirect('Logout')

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
def BuyersApplicationApprove(request, pk, email,lot_type,phase,block,lotno,fullname):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = BuyersFormModel.objects.filter(email=email).values_list('email', flat=True).first()
        lot = BuyersFormModel.objects.filter(lot_type=lot_type).values_list('lot_type', flat=True).first()
        p = BuyersFormModel.objects.filter(phase=phase).values_list('phase', flat=True).first()
        b1 = BuyersFormModel.objects.filter(block=block).values_list('block', flat=True).first()
        l = BuyersFormModel.objects.filter(lotno=lotno).values_list('lotno', flat=True).first()
        fname = BuyersFormModel.objects.filter(fullname=fullname).values_list('fullname', flat=True).first()
        send_mail(
                'From Himlayang General Trias Management',
                f'Dear {fname},\n\nGood day!\n\n' +
                f'We want to inform you that we have approved your request upon checking on it. {lot} Phase:{p} Block{b1} Lot:{l} is available. Thank you for buying lots at the Himlayang General Trias Cemetery.\n\n'+
                'If you need immediate assistance or have any further questions, you can make an appointment with the Office of Himlayang Gen. Trias and free to call us at Tel. #: (046) 419-8380 to 89 (02) 8779-5980 or visit our website: www.generaltrias.gov.ph.\n\n'+
                'Regards,\nGeneral Trias Management',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        BuyersFormModel.objects.filter(pk=pk).update(
            lot_type=None,phase=None,block=None,terms=None,fullname=None,age=None,gender=None,contacts=None,address=None,email=None)
        return redirect('BuyersApplication', pk=c, email=email)
    else:
        return redirect('Logout')

@login_required(login_url='/accounts/login/')
def BuyersApplicationReject(request, pk, email,lot_type,phase,block,lotno,fullname):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = BuyersFormModel.objects.filter(email=email).values_list('email', flat=True).first()
        lot = BuyersFormModel.objects.filter(lot_type=lot_type).values_list('lot_type', flat=True).first()
        p = BuyersFormModel.objects.filter(phase=phase).values_list('phase', flat=True).first()
        b1 = BuyersFormModel.objects.filter(block=block).values_list('block', flat=True).first()
        l = BuyersFormModel.objects.filter(lotno=lotno).values_list('lotno', flat=True).first()
        fname = BuyersFormModel.objects.filter(fullname=fullname).values_list('fullname', flat=True).first()
        send_mail(
                'From Himlayang General Trias Management',
                f'Dear {fname},\n\nGood day!\n\n' +
                f'We want to inform you that we have declined your request upon checking on it. {lot} Phase:{p} Block:{b1} Lot:{l} is already taken, try to acquire other lots. We highly appreciate your interest on purchasing a lot at Himlayang General Trias Cemetery and we are terribly sorry for the inconvenience.\n\n'+
                'If you need immediate assistance or have any further questions, you can make an appointment with the Office of Himlayang Gen. Trias and free to call us at Tel. #: (046) 419-8380 to 89 (02) 8779-5980 or visit our website: www.generaltrias.gov.ph.\n\n'+
                'Regards,\nGeneral Trias Management',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        BuyersFormModel.objects.filter(pk=pk).update(
            lot_type=None,phase=None,block=None,terms=None,fullname=None,age=None,gender=None,contacts=None,address=None,email=None)
        return redirect('BuyersApplication', pk=c, email=email)
    else:
        return redirect('Logout')

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
def AppointmentApprove(request, pk, email,date,fullname):
    if request.user.is_authenticated and request.user.is_admin:
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = BookAppointmentModel.objects.filter(email=email).values_list('email', flat=True).first()
        date = BookAppointmentModel.objects.filter(date=date).values_list('date', flat=True).first()
        fname = BookAppointmentModel.objects.filter(fullname=fullname).values_list('fullname', flat=True).first()
        send_mail(
                'From Himlayang General Trias Management',
                f'Dear {fname},\n\nGood day!\n\n'+
                f'Thanks for reaching out to us. We appreciate your interest in Himlayang General Trias Cemetery. This is to confirm that we have successfully received your request for Appointment. We are pleased to inform you that you have been appointed on the {date}. Please arrive at General Trias City Hall at least 30 minutes before your scheduled appointment time. \n\n'+
                'If you need immediate assistance or have any further questions, feel free to call us at Tel. #: (046) 419-8380 to 89 (02) 8779-5980 or visit our website: www.generaltrias.gov.ph.\n\n'+
                'Sincery,\n\nGeneral Trias Managemanent',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        BookAppointmentModel.objects.filter(pk=pk).update(reason=None,fullname=None,contacts=None,email=None,date=None)
        return redirect('Appointment', pk=c, email=email)
    else:
        return redirect('Logout')
 
@login_required(login_url='/accounts/login/')
def AppointmentReject(request,pk,email,fullname):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = BookAppointmentModel.objects.filter(email=email).values_list('email', flat=True).first()
        fname = BookAppointmentModel.objects.filter(fullname=fullname).values_list('fullname', flat=True).first()
        send_mail(
                'From Himlayang General Trias Management',
                f'Hello {fname},\n\n'+
                'Thanks for reaching out to us. We appreciate your interest in Himlayang Gen. Trias Cemetery. After reviewing your request date. It turned out that we were fully booked on that day. We regret to inform you that your appointment request has been denied. \n\n'+
                'If you need immediate assistance or have any further questions, feel free to call us at Tel. #: (046) 419-8380 to 89 (02) 8779-5980 or visit our website: www.generaltrias.gov.ph.\n\n'+
                'Sincerely,\n\nGeneral Trias Managemanent',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        BookAppointmentModel.objects.filter(pk=pk).update(reason=None,fullname=None,contacts=None,email=None,date=None)
        return redirect('Appointment', pk=c, email=email)
    else:
        return redirect('Logout')

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
def InquiryApprove(request, pk, email, lot_type,phase,block,lotno,fullname):
    if request.user.is_authenticated and request.user.is_admin:
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = InquiryFormModel.objects.filter(email=email).values_list('email', flat=True).first()
        lot = InquiryFormModel.objects.filter(lot_type=lot_type).values_list('lot_type', flat=True).first()
        p = InquiryFormModel.objects.filter(phase=phase).values_list('phase', flat=True).first()
        b1 = InquiryFormModel.objects.filter(block=block).values_list('block', flat=True).first()
        l = InquiryFormModel.objects.filter(lotno=lotno).values_list('lotno', flat=True).first()
        fname = InquiryFormModel.objects.filter(fullname=fullname).values_list('fullname', flat=True).first()
        send_mail(
                'From Himlayang General Trias Management',
                f'Dear {fname},\n\nGood day!\n\n' +
                f'We want to inform you that we have approved your request upon checking on it. {lot} Phase:{p} Block:{b1} Lot:{l} is available. Thank you for inquiring at the Himlayang General Trias Cemetery.\n\n'+
                'If you need immediate assistance or have any further questions, you can make an appointment with the Office of Himlayang Gen. Trias and free to call us at Tel. #: (046) 419-8380 to 89 (02) 8779-5980 or visit our website: www.generaltrias.gov.ph.\n\n'+
                'Regards,\nGeneral Trias Management',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        InquiryFormModel.objects.filter(id=pk).delete()
        return redirect('Inquiry',pk=pk, email=email)
    else:
        return redirect('Logout')
@login_required(login_url='/accounts/login/')
def InquiryReject(request,pk,email,lot_type,phase,block,lotno,fullname):
    if request.user.is_authenticated and request.user.is_admin:
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = InquiryFormModel.objects.filter(email=email).values_list('email', flat=True).first()
        lot = InquiryFormModel.objects.filter(lot_type=lot_type).values_list('lot_type', flat=True).first()
        p = InquiryFormModel.objects.filter(phase=phase).values_list('phase', flat=True).first()
        b1 = InquiryFormModel.objects.filter(block=block).values_list('block', flat=True).first()
        l = InquiryFormModel.objects.filter(lotno=lotno).values_list('lotno', flat=True).first()
        product = (lot + ' Phase:'+p+ ' Block:'+b1+ ' Lot:'+l + ' is Unavailable')
        fname = InquiryFormModel.objects.filter(fullname=fullname).values_list('fullname', flat=True).first()
        send_mail(
                'From Himlayang General Trias Management',
                f'Dear {fname},\n\nGood day!\n\n' +
                f'We want to inform you that we have declined your request upon checking on it. {lot} Phase:{p} Block:{b1} Lot:{l} is already taken, try to inquire other lots. Thank you for inquiring at the Himlayang General Trias Cemetery.\n\n'+
                'If you need immediate assistance or have any further questions, you can make an appointment with the Office of Himlayang Gen. Trias and free to call us at Tel. #: (046) 419-8380 to 89 (02) 8779-5980 or visit our website: www.generaltrias.gov.ph.\n\n'+
                'Regards,\nGeneral Trias Management',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        InquiryFormModel.objects.filter(id=pk).delete()
        return redirect('Inquiry',pk=pk, email=email)
    else:
        return redirect('Logout')

@login_required(login_url='/accounts/login/')
def Application(request,pk,email):
    if request.user.is_authenticated and request.user.is_admin:
        print ("Application Page")
        a = User.objects.filter(pk=pk)
        applicants_table = ApplicationFormModel.objects.exclude(fullname=None)
        myFilter = applicationFilter(request.GET, queryset=applicants_table)
        applicants_table = myFilter.qs
    else:
        return redirect('Logout')
    return render(request, 'files/Application.html',{'a':a, 'applicants_table':applicants_table, 'myFilter':myFilter})

@login_required(login_url='/accounts/login/')
def ApplicationApprove(request,pk,email, phase, block, lotno, fullname):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = ApplicationFormModel.objects.filter(email=email).values_list('email', flat=True).first()
        p = ApplicationFormModel.objects.filter(phase=phase).values_list('phase', flat=True).first()
        b1 = ApplicationFormModel.objects.filter(block=block).values_list('block', flat=True).first()
        l= ApplicationFormModel.objects.filter(lotno=lotno).values_list('lotno', flat=True).first()
        fname = ApplicationFormModel.objects.filter(fullname=fullname).values_list('fullname', flat=True).first()
        send_mail(
                'From Himlayang General Trias Management',
                f'Dear {fname},\n\nGood day!\n\n' +
                f'We want to inform you that we have approved your request upon checking on it. The Apartment Unit Phase:{p} Block:{b1} Lot:{l} is available. Thank you for buying lots at the Himlayang General Trias Cemetery.\n\n'+
                'If you need immediate assistance or have any further questions, you can make an appointment with the Office of Himlayang Gen. Trias and free to call us at Tel. #: (046) 419-8380 to 89 (02) 8779-5980 or visit our website: www.generaltrias.gov.ph.\n\n'+
                'Regards,\nGeneral Trias Management',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        ApplicationFormModel.objects.filter(pk=pk).update(
            date=None,phase=None,block=None,lotno=None,fullname=None,age=None,gender=None,contacts=None,address=None,email=None)
        return redirect('Application', pk=c, email=email)
    else:
        return redirect('Logout')

@login_required(login_url='/accounts/login/')
def ApplicationReject(request,pk,email, phase, block, lotno, fullname):
    if request.user.is_authenticated and request.user.is_admin:
        a = User.objects.filter(pk=pk)
        c = User.objects.filter(pk=pk).values_list('id', flat=True).first()
        b = ApplicationFormModel.objects.filter(email=email).values_list('email', flat=True).first()
        p = ApplicationFormModel.objects.filter(phase=phase).values_list('phase', flat=True).first()
        b1 = ApplicationFormModel.objects.filter(block=block).values_list('block', flat=True).first()
        l= ApplicationFormModel.objects.filter(lotno=lotno).values_list('lotno', flat=True).first()
        fname = ApplicationFormModel.objects.filter(fullname=fullname).values_list('fullname', flat=True).first()
        send_mail(
                'From Himlayang General Trias Management',
                f'Dear {fname},\n\nGood day!\n\n' +
                f'We want to inform you that we have declined your request upon checking on it. The Apartment Unit Phase:{p} Block:{b1} Lot:{l} is already taken, try to acquire other lots. We highly appreciate your interest on purchasing a lot at Himlayang General Trias Cemetery and we are terribly sorry for the inconvenience.\n\n'+
                'If you need immediate assistance or have any further questions, you can make an appointment with the Office of Himlayang Gen. Trias and free to call us at Tel. #: (046) 419-8380 to 89 (02) 8779-5980 or visit our website: www.generaltrias.gov.ph.\n\n'+
                'Regards,\nGeneral Trias Management',
                'andrewleilaraqueljustin@gmail.com',
                [b],
                fail_silently=False
            )
        ApplicationFormModel.objects.filter(pk=pk).update(
            date=None,phase=None,block=None,lotno=None,fullname=None,age=None,gender=None,contacts=None,address=None,email=None)
        return redirect('Application', pk=c, email=email)
    else:
        return redirect('Logout')

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
                'From Himlayang General Trias Management',
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
    q = ""
    if 'q' in request.GET:
        q=request.GET['q']
        if q =='':
            return render(request, 'files/GraveFinder.html')
        else:
            prod = Product.objects.filter(deceased__icontains=q).order_by('-id')
            p = Paginator(prod, per_page=8)
            page = request.GET.get('page')
            if page == None or page == "":
                page = "1"
            prod = p.get_page(page)
            prod.adjusted_elided_pages = p.get_elided_page_range(page)
            return render(request, 'files/GraveFinder.html',{'prod':prod,'q':q })
    else:
        return render(request, 'files/GraveFinder.html')

    # p = Paginator(prod, per_page=8)
    # page = request.GET.get('page')
    # if page == None or page == "":
    #     page = "1"
    # prod = p.get_page(page)
    # prod.adjusted_elided_pages = p.get_elided_page_range(page)
    # return render(request, 'files/GraveFinder.html',{'prod':prod,'q':q })

def InquiryForm(request):
    form = InquiryFormForm()
    if 'lots' in request.GET:
        q=request.GET['lots']
        available = LotOrder.objects.filter(product_id__lot__icontains=q,terms=None).order_by('-product')
    else:
        available = LotOrder.objects.all().filter(terms=None).order_by('-product')
    p = Paginator(available, per_page=16)
    page = request.GET.get('page')
    if page == None or page == "":
        page = "1"
    avail = p.get_page(page)
    avail.adjusted_elided_pages = p.get_elided_page_range(page)
    if request.method == 'POST':
        form = InquiryFormForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success'),
            fail_silently=True,
            return redirect('InquiryForm')
        else:
            messages.error(request, 'Error'),
            fail_silently=True,
            return redirect('InquiryForm')
    return render(request, 'files/InquiryForm.html',{'form':form,'available':available,'avail':avail})

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