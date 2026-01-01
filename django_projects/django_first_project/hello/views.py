# importing required libraries
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# creating a function that returns a http response
def index(request):
    return render(request, "hello/index.html")

def gaurav(request):
    return HttpResponse("Hello, Gaurav!")

#creating a function that takes a variable
def greet(request, name):
    return HttpResponse(f"Hello, {name}!") # returns name with spaces as well

# creating a function that renders a whole file
# this works when there aren't two paths pointing to the same file, if so comment one out and use only one.
# the urlspattern in the apps urls.py file is in order so what comes first is used, so urls need to be planned in order of precedence
def rend_file(request):
    return render(request, "hello/index.html")

"""Creating another function that is similar to the greet function we created above but it renders an
html file and also has a third part which is called a context. This context for this particular function is
a dictionary that takes the name as the key and then uses the capitalize function to capitalize the argument we
have on the function."""
def greet2(request, name):
    print("greet2 is being called") # for debugging and learning purposes
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })