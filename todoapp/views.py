from django.shortcuts import render, redirect
from django.http import HttpResponse

#For register
from django.contrib.auth.forms import UserCreationForm
#For login
from django.contrib.auth import authenticate, login, logout
#login decorators
from django.contrib.auth.decorators import login_required
#For flash messages
from django.contrib import messages

from .models import *
from .forms import *

# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Guest.objects.create(
                user=user, 
                name=user.username
                )
            print('profile created!')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'todoapp/register.html', context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('todo')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'todoapp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    guests = request.user.guest.list_set.all()
    guest = Guest.objects.get(user=request.user)
    lists = List.objects.all()
    initial_data = {'guest': guest}
    form = ListForm(initial=initial_data)
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            list_instance = form.save(commit=False)
            list_instance.guest = guest
            list_instance.save()
            return redirect('/')
    context = {'lists': lists, 'form': form, 'guests':guests}
    return render(request, 'todoapp/todo.html', context)

@login_required(login_url='login')
def updateList(request, pk):
    guests = request.user.guest.list_set.all()
    lists = List.objects.all()
    listId = List.objects.get(id=pk)
    form = ListForm(instance=listId)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=listId)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'lists': lists, 'guests':guests}
    return render(request, 'todoapp/todo.html', context)

@login_required(login_url='login')
def deleteList(request, pk):
    listId = List.objects.get(id=pk)
    if request.method == 'POST':
        listId.delete()
        return redirect('/')
    context = {'listId':listId}
    return render(request, 'todoapp/delete.html', context)

