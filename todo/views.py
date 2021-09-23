from django.shortcuts import render, HttpResponse

# Create your views here.
# def say_hello(request):
    # return HttpResponse("Hello!") #Change to use render now that we hav e created todo_list.html template, see new function get_todo_list below

def get_todo_list(request):
    return render(request, 'todo/todo_list.html')