from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http.response import HttpResponse

def Homepage(request):
    return render(request, 'files/Homepage.html')

