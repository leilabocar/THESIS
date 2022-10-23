from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http.response import HttpResponse

def index(request):
    return HttpResponse('Homepage')

