from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HTTPResponse('Homepage')

