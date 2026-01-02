from django.urls import path
from . import views

# this lets django know that this is for the tasks app
app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]