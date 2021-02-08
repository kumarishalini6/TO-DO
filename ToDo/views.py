from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.


def index(request):
    tasks = Tasks.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'task': tasks, 'form': form}
    return render(request, 'index.html', context)


def update(request , id):
    task = Tasks.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'update.html' , context)


def delete(request , id):
    task = Tasks.objects.get(id=id)
    task.delete()
    return redirect('/')

