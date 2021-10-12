# Get Todo model
from .models import Todo
from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# The view function is provided with a (request) object
def index(request):
    # Handle a POST request from index.html form
   if request.method == 'POST':
       # If there's a POST req., get the text field out of the (request) obj
      text = request.POST["text"]

       # Create an object instance of the Todo() class
      todo = Todo()

       # Set the text prop on the obj
      todo.user = request.user
      todo.text = text

      # Save the todo object into the database --> auto PK created
      todo.save()

      # Get a list of all the todo items in the database
      #todos = Todo.objects.all()

   # Filter the query & Show the undone todo items
   todos = Todo.objects.filter(status=False).filter(user=request.user)

   # Put the list of items into a context dictionary
   context = {
            'todos': todos
   }
   return render(request, 'todo_app/index.html', context)


@login_required
# View function for the completed todos page
def change_status(request):
   # Get PK from the (request) object, shown as the hidden input in HTML
   # To find the todo item
   pk = request.POST["pk"]

   # Get the todo item from the database with the shortcut function
   todo = get_object_or_404(Todo, pk=pk, user=request.user)

   # Check the checkbox
   if "checked" in request.POST:
      todo.status = True
   else:
      todo.status = False
   todo.save()

   # Return the user to the index view after marking todo item completed
   return HttpResponseRedirect(reverse('todo_app:index'))


@login_required
# View function for Completed todo list & Handle the request from urls.py
def completed_todos(request):
   # Filter the query & Show completed todo items
   todos = Todo.objects.filter(status=True).filter(user=request.user)
   context = {
      'todos' : todos
   }
   # Take user to the Completed todo page
   return render(request, 'todo_app/completed_todos.html', context)


@login_required
# View function for Deleted todo list
def delete_todo(request):
   # Delete on Index & Completed pages
   # Tthe referring url from META prop of the (request) obj
   print(request.META['HTTP_REFERER'])
   pk = request.POST["pk"]
   todo = get_object_or_404(Todo, pk=pk, user=request.user)
   todo.delete()

   # Get the url from META prop & redirect back to the referring page
   if request.META['HTTP_REFERER'].split('/')[-2] == 'todo':
      return HttpResponseRedirect(reverse('todo_app:index'))
   else:
       return HttpResponseRedirect(reverse('todo_app:completed_todos'))
