from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('<h1>Hello world!</h1><br><a href="directories/">Справочники</a><br><a href="products/">Книги</a>' )