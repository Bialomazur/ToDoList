from django.shortcuts import render
from . import models
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Todo

# Create your views here.

def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    print(todo_items)
    return render(request, "ToDoList/index.html", {"todo_items" : todo_items})

def add_item(request):

    date = timezone.now()
    content = request.POST["content"]
    print(content)
    task = Todo.objects.create(added_date=date, text=content)
    print(task)
    return HttpResponseRedirect("/")

def delete_item(request, item_id):

    Todo.objects.get(id=item_id).delete()
    return HttpResponseRedirect("/")
