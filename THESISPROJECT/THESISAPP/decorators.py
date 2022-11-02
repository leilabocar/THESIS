from django.http import HttpResponse
from django.shortcuts import redirect, render

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        
        if request.user.is_authenticated and request.user.is_admin:
            return redirect('AdminHomepage')
        elif request.user.is_authenticated and request.user.is_client:
            return redirect('Client')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func