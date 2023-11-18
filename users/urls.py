from django.urls import path
from .views import home, register

app_name = 'users'

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register')
    # Add more URL patterns as needed
]
