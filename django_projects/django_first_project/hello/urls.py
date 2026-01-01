# import requried libraries
from django.urls import path

"""The . here means the current directory and get it from the
current directory. Importing this to get the function we need
from the file"""
from . import views

"""The empty string means nothing after the url and the original path of the url.
The second part is the part where we tell it what the view we want is, in this case
we want it to return the index function so we use the views.index since the function is
inside the views.py file and finally we give this path a name. It is optional but having
a name comes in handy for other purposes so it is recommended to have one if possible."""
urlpatterns = [
    # path("", views.index, name="index"),
    path("gaurav", views.gaurav, name="gaurav"),
    path("rend_file", views.rend_file, name="rend_file"),
    path("<str:name>", views.greet2, name="greet2"),
    path("<str:name>", views.greet, name="greet"),
    
]