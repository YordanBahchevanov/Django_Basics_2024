from django.shortcuts import render
from djangoIntroduction.todo_app.models import Task


def index(request):
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
    }

    return render(request, 'tasks/index.html', context)  # MIME TYPE text/html
