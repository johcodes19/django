

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms


# Create your views here.
# a class to represent the form

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    tasks = request.session["tasks"]
    return render(request, 'todo/index.html', {
        "tasks": tasks,
    })


def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks = request.session.get("tasks", [])
            tasks.append(task)
            request.session["tasks"] = tasks
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request, 'todo/add.html', {
                "form": form
            })
    return render(request, 'todo/add.html', {
        # a variable for the above form
        "form": NewTaskForm()
    })
