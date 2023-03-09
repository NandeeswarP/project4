from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sample(request):
    return HttpResponse('<h1>HI, THIS IS DJANGO PROJECT</h1>')

def sam(request):
    return HttpResponse('<em>DJANGO</em>')
