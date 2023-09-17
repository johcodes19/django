#you need to import httpResponse from django.http
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#you need to create a function that will send the http request
def request(request):#I have just named the function as request but the parameter request is inbuilt
    return HttpResponse("Hello, world!")

def sayhi(request):
    return HttpResponse("Hello Margarita")


