from django.shortcuts import get_object_or_404, render

from .models import Task

# Create your views here.

def index(request):
	to_do_list = Task.objects.all() 
	context = {
		"to_do_list": to_do_list,
	}
	return render(request, "to_do_list/index.html", context)


def task_detail(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	context = {
		"task": task
	}
	return render(request, "to_do_list/task_detail.html", context)