from django.shortcuts import render
from django import forms

tasks = ["foo", "bar", "baz"]

class new_task_form(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        form = new_task_form(request.POST) # if this is left empty then it just creates a blank form
        # when we use request.POST to fill this class object then it takes the information that the user inputted in the form
        # and then assigns that value to this variable.

        if form.is_valid(): # checking if the form is valid
            task = form.cleaned_data["task"] # we are cleaning the data and then only taking the task from the cleaned data
            tasks.append(task) # now we take that cleaned data task and append it to our tasks list created before
            
        else: # if the data is not valid, then we return the same form back to the user
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": new_task_form()
    })