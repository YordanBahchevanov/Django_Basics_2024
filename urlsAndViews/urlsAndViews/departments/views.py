from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Hello World!<h1/>")


def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args}, Kwargs: {kwargs}<h1/>")


def view_with_name(request, variable):  # should be named the same way as the urls
    return HttpResponse(f"<h1>Variable: {variable}<h1/>")


def view_with_int_pk(request, pk: int):
    return HttpResponse(f"<h1>Int pk with pk: {pk}</h1>")
