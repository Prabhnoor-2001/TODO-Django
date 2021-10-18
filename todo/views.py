from django.shortcuts import redirect, render
from .models import Todo
import sys
# Create your views here.
def index(request):
    todo= Todo.objects.all()
    print(todo, file=sys.stderr)
    if request.method == 'POST':
        newTodo = Todo( title = request.POST['title'])
        newTodo.save()
        return redirect('/')
    return render(request, 'index.html',{'todos': todo})

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
