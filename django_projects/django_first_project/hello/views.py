# importing required libraries
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# creating a function that returns a http response
def index(request):
    return HttpResponse("Hello!") 

def gaurav(request):
    return HttpResponse("Hello, Gaurav!")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")

"""So if I want to load a whole html file, adding that between two strings,
don't make sense. So, to make it better, we can use the render function to render
requests and the file we need to load in the webserver. See below function for example"""

def indexs(request):
    return render(request, "hello/index.html") # here we are passing both the request and the template file we want 