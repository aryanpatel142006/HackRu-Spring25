from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def reverse_string(Request):
    return HttpResponse("Hello from django!")