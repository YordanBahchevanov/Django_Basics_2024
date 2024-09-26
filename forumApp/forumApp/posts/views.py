from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from forumApp.posts.forms import PostForm


def index(request):

    context = {
        "my_form": "",
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


def add_post(request):
    form = PostForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        "form": form,
    }

    return render(request, 'posts/add-post.html', context)
















