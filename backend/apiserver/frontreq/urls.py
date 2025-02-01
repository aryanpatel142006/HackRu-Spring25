# my_app/urls.py
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('reverse_string/', views.reverse_string, name='reverse_string'),  # Example URL pattern
]