from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .admin import models_list

def get_directory(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'directory/all_refs.html', context=context)

def get_detailed_directory_view(request, author_id):
    author_obj = Author.objects.get(pk = author_id)
    context = {
        'author': author_obj
    }
    return render(request, 'directory/ref_items.html', context=context)