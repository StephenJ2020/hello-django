from django.shortcuts import render, HttpResponse
from .models import Items

# Create your views here.
# def say_hello(request):
# return HttpResponse("Hello!") #Change to use render now that we have
# created todo_list.html template, see new function get_todo_list below


def get_todo_list(request):
    items = Items.objects.all()
    context = {
        "items": items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    return render(request, 'todo/add_item.html')
    