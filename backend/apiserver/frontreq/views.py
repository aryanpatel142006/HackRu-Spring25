from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status  # Import status codes

# Create your views here.

@api_view(['GET'])  # Only allow GET requests
def reverse_string(request):
    my_string = "Hello from my Django!"  # The string you want to return
    return Response(my_string, status=status.HTTP_200_OK, content_type='text/plain') # important to add content type.