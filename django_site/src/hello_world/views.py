from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('<h1>Hello World!</h1>')
