from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Task

# Create your views here.


def index(request):
    # Query tasks
    to_do_list = Task.objects.all()
    to_do_list_sorted_by_deadline = Task.objects.order_by("deadline")
    context = {
        "to_do_list": to_do_list,
        "to_do_list_sorted_by_deadline": to_do_list_sorted_by_deadline,
    }

    # Create a form instance with the POST data
    if request.method == "POST":
        new_task_name = request.POST.get("name")
        new_task_description = request.POST.get("description")
        new_task_deadline = request.POST.get("deadline")

        # Create the new task
        new_task = Task(
            name=new_task_name,
            description=new_task_description,
            deadline=new_task_deadline,
        )
        new_task.save()
        return redirect("index")

    return render(request, "to_do_list/index.html", context)


def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {"task": task}

    # Handle form
    if request.method == "POST":
        edit_task_name = request.POST.get("name")
        edit_task_description = request.POST.get("description")
        edit_task_deadline = request.POST.get("deadline")

        # Change task
        task = Task.objects.get(pk=task_id)
        task.name = edit_task_name
        task.description = edit_task_description
        task.deadline = edit_task_deadline
        task.save()
        return HttpResponseRedirect(reverse("index"))


    return render(request, "to_do_list/edit-task.html", context)
