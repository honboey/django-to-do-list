from django.shortcuts import render

from .models import Task

# Create your views here.

def index(request):
	to_do_list = Task.objects.all() 
	context = {
		"to_do_list": to_do_list,
	}
	return render(request, "to_do_list/index.html", context)