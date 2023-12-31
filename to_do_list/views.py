from django.forms import ValidationError
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
        # Add a task
        if request.POST.get("form-id") == "add-task":
            try:
                new_task = Task(
                    name=request.POST.get("name"),
                    description=request.POST.get("description"),
                    deadline=request.POST.get("deadline"),
                )
                if not new_task.deadline:
                    raise(ValidationError("You suck"))
            except(ValidationError):
                context["error_message"] = "You did not supply a valid deadline"
                return render(request, "to_do_list/index.html", context)
            else:
                new_task.save()
                return render(request, "to_do_list/index.html", context)

        # Delete a task
        if request.POST.get("form-id") == "delete-task":
            task_to_delete = Task.objects.get(pk=request.POST.get("task-id"))
            task_to_delete.delete()
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
