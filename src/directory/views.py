from django.shortcuts import render
from django.http import HttpResponse

def get_directory(request):
    return HttpResponse('<h1>Здесь будет страница со справочниками</h1>')
