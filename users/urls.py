# users -> urls.py
from django.urls import path
from .views import home, register
from users.views import firebase_authenticate


app_name = 'users'

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('firebase_authenticate/', firebase_authenticate, name='firebase_authenticate'),

    # Add more URL patterns as needed
]
