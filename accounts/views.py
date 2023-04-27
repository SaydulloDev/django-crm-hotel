from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import UserProfileForm


# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Account Not Found')
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        if not all(request.POST.values()):
            messages.error(request, 'Please fill out all fields')
            return redirect('register')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already registered')
            return redirect('register')

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
    return render(request, 'accounts/register.html')


@login_required
def profile_view(request):
    return render(request, "accounts/profile.html", {"user": request.user})


def profile_edit_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'accounts/profile_update.html', {'form': form})
