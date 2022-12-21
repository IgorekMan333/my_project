from django.shortcuts import render, redirect
from .forms import CreateUserForm, TaskForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url='log')
def index(request):
	tasks = Task.objects.all()
	form = TaskForm()
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	context = {
        'tasks': tasks,
        'form': form
    }
	return render(request, 'list.html', context)


@login_required(login_url='log')
def updateTask(request, pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('index')
	return render(request, 'update_task.html', {'form':form})


@login_required(login_url='log')
def deleteTask(request, pk):
	item = Task.objects.get(id=pk)
	if request.method == 'POST':
		item.delete()
		return redirect('index')
	return render(request, 'delete.html', {'item': item})


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('log')
    return render(request, 'register.html', {'form': form})


def log(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                return redirect('index')
    return render(request, 'log.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('log')


