from datetime import timedelta, datetime

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from colors.models import Color
from core.models import Todo
from priorities.models import Priority
from status.models import Status


@login_required(login_url='/login/')
def list(request):
    user = request.user
    todos = Todo.objects.filter(user = user, due_date__gt = datetime.now()).exclude(status = '3') | Todo.objects.filter(user = user, due_date = None).exclude(status = '3')
    return render(request, 'todo_list.html', {'todos': todos})

@login_required(login_url='/login/')
def completed(request):
    user = request.user
    todos = Todo.objects.filter(user = user, status = '3')
    return render(request, 'todo_list.html', {'todos': todos})

@login_required(login_url='/login/')
def add(request):
    id_todo = request.GET.get('id')

    dados = {}
    dados['statuses'] = Status.objects.all()
    dados['priorities'] = Priority.objects.all()
    dados['colors'] = Color.objects.all()

    if id_todo:
        dados['todo'] = Todo.objects.get(id=id_todo)

    return render(request, 'todo_add.html', dados)


@login_required(login_url='/login/')
def save(request):
    if request.POST:
        user = request.user

        task = request.POST.get('task')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date') if request.POST.get('due_date') else None
        description = request.POST.get('description')
        color = request.POST.get('color')

        if request.POST.get('id'):
            id = request.POST.get('id')
            todo = Todo.objects.get(id=id)

            if user == todo.user:
                todo.task = task
                todo.status = status
                todo.priority = priority
                todo.description = description
                todo.color = color
                todo.due_date = due_date

                todo.save()
        else:
            try:
                Todo.objects.create(
                    task = task,
                    status = status,
                    priority = priority,
                    due_date = due_date,
                    description = description,
                    color = color,
                    user = user
                )
            except Exception:
                raise Http404()
        return redirect('/')

    else:
        statuses = Status.objects.all()
        priorities = Priority.objects.all()
        colors = Color.objects.all()
        return render(request, 'todo_add.html', {'statuses': statuses, 'priorities': priorities, 'colors': colors, })

@login_required(login_url='/login/')
def delete(request, todo_id):
    user = request.user
    try:
        todo = Todo.objects.get(id=todo_id)
    except Exception:
        raise Http404()

    if user == todo.user:
        todo.delete()
    else:
        raise Http404()

    return redirect('/')
