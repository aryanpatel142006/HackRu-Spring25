from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status  # Import status codes

# Create your views here.

def reverse_string(Request):
    return HttpResponse("Hello from django")