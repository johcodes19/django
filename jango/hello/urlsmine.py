#this one is mine
#you need to first import path from django.urls
from django.urls import path
#you also need to import views from the current directory
from . import views
urlpatterns =[
    path("", views.request, name="request"),
    path("sayhi", views.sayhi, name="sayhi"),
]