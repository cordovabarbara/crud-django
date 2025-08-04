from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def task_list_and_create(request):
    form = TaskForm()
    tasks = Task.objects.all()

    return render(request, 'task_list.html',{
        'form':form,
        'tasks':tasks
    })