from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
    lists = List.objects.all()
    form = ListForm()
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'lists': lists, 'form': form}
    return render(request, 'todoapp/todo.html', context)

def updateList(request, pk):
    lists = List.objects.all()
    listId = List.objects.get(id=pk)
    form = ListForm(instance=listId)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=listId)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'lists': lists}
    return render(request, 'todoapp/todo.html', context)

def deleteList(request, pk):
    listId = List.objects.get(id=pk)
    if request.method == 'POST':
        listId.delete()
        return redirect('/')
    context = {'listId':listId}
    return render(request, 'todoapp/delete.html', context)

