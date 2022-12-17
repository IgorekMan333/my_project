from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Employees


@login_required(login_url='log')
def home(request):
    units = Employees.objects.select_related('office').all()
    contex = {
        'units': units
    }
    return render(request, 'home.html', contex)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('log')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def log(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'log.html', context)


def logoutUser(request):
    logout(request)
    return redirect('log')

