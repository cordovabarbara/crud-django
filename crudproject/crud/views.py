from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list_and_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:crud_list')
    else:
        form = TaskForm()
    #tasks = Task.objects.all()
    completed_tasks = Task.objects.filter(completed=True)
    incompleted_tasks = Task.objects.filter(completed=False)

    return render(request, 'task_list.html',{
        'form':form,
        'completed_tasks':completed_tasks,
        'incompleted_tasks': incompleted_tasks
        
        
        #'tasks':tasks
    })