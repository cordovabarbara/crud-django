from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
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
        #'tasks':tasks
        'completed_tasks':completed_tasks,
        'incompleted_tasks': incompleted_tasks
    })
    
#toggle
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
        return redirect('crud:crud_list')

#edit Task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('crud:crud_list')
    else:
        form = TaskForm(instance=task)
        
    return render(request,'edit_task.html', {'form':form})

#Delete
def delete_task(request, task_id):
        task = get_object_or_404(Task, id=task_id)
        
        if request.method == 'POST':
            task.delete()
            return redirect('crud:crud_list')