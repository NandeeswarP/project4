from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def a(request):
    return HttpResponse('<h1>ABCD</h1>')

def b(request):
    return HttpResponse('hi, hello!')

def h(request):
    return HttpResponse('NANDEESWAR')
