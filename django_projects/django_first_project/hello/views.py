# importing required libraries
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# creating a function that returns a http response
def index(request): # only having the render here for index.html seems to work
    return render(request, "hello/index.html")

def gaurav(request):
    return HttpResponse("Hello, Gaurav!")

#creating a function that takes a variable
def greet(request, name):
    return HttpResponse(f"Hello, {name}!") # returns name with spaces as well

# creating a function that renders a whole file, this for some reason doesn't work
def rend_file(request):
    return render(request, "hello/index.html")