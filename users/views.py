from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import firebase_admin
from firebase_admin import auth
from django.http import JsonResponse


def firebase_authenticate(request):
    if request.method == 'GET':
        # Handle GET request
        return JsonResponse({'message': 'This is a GET request.'})
    elif request.method == 'POST':
        # Handle POST request
        id_token = request.POST.get('idToken')  # Adjust the field name based on your frontend data
        try:
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']
            user = authenticate(firebase_uid=uid)  # Create a custom authentication backend
            login(request, user)
            return JsonResponse({'message': 'Authentication successful.'})
        except auth.InvalidIdTokenError:
            return JsonResponse({'error': 'Invalid ID token.'})


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:home')  # Replace 'home' with your home view name
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
    