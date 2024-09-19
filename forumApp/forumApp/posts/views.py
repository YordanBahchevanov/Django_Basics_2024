from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    context = {
        "current_time": datetime.now(),
        "some_text": "Hello my name is Yordan, and I am and architect",
        "another_text": "Hi",
        "users": [
            "Ivan",
            "dancho",
            "Dani",
            "mecho",
            "Pooh",
        ]
    }

    return render(request, 'base.html', context)


def dashboard(request):

    context = {
        "posts": [
            {
                "title": "How to create django project?",
                "author": "Yordan",
                "content": "I am learning how to create django project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 1?",
                "author": "Daniela",
                "content": "",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 2?",
                "author": "",
                "content": "I am **learning** how to create django project",
                "created_at": datetime.now(),
            }
        ]
    }

    return render(request, 'posts/dashboard.html', context)
