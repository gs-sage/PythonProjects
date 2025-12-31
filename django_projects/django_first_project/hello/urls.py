from django.urls import path

"""The . here means get it from the current directory.
importing this to get the function we need from the file.
"""
from . import views 

"""the empty string means nothing after the url,
the second part is the part where we tell it what view we want, in 
this case we want it to return the index function so we use views.index 
since the function is inside the views.py file and finally we give this path 
a name. It is optional but having a name comes in handy for other purposes so
it is recommended to have it."""

urlpatterns = [
    path("", views.index, name="index") 
]