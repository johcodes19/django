from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hellow/index.html" )

def tiger(request):
    return HttpResponse("Hola tigra, como estas")

def greetings(request, name):
    return render(request,"hellow/greet.html", {
        "name": name.title()
    })