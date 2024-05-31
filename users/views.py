from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'users/home.html', {'title': 'For Landlords'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
