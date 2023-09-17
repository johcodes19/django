from django.shortcuts import render

# Create your views here.
tasks = ['wash utensils', 'do laundry', 'clean the garage']
def index(request):
    return render(request, 'todo/index.html',{
        'tasks':tasks,
        
    }
                )

def add(request):
    return render(request, 'todo/add.html')