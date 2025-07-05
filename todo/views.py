from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from datetime import date

def Task_list(request):
    filter_val = request.GET.get('filter', 'all')

    if filter_val == 'completed':
        Tasks = Task.objects.filter(Completed=True).order_by('DueDate', 'id')
    elif filter_val == 'pending':
        Tasks = Task.objects.filter(Completed=False).order_by('DueDate', 'id')
    else:
        Tasks = Task.objects.all().order_by('Completed', 'DueDate', 'id')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Task_list')

    return render(request, 'Task_list.html', {
        'Tasks': Tasks,
        'today': date.today()
    })

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.Completed = not task.Completed
        task.save()
    return redirect('Task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('Task_list')

def mark_all_completed(request):
    Task.objects.update(Completed=True)
    return redirect('Task_list')

def delete_all(request):
    Task.objects.all().delete()
    return redirect('Task_list')

def clear_completed(request):
    Task.objects.filter(Completed=True).delete()
    return redirect('Task_list')
