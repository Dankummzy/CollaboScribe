from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


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
    