from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {"tasks": tasks })

def create_task(request):
   task = Task(name=request.POST['name'], description=request.POST['description'], department=request.POST['department'], direcction=request.POST['direcction'], color=request.POST['color'])
   task.save()
   return redirect('/tasks/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')