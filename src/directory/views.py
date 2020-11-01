from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .admin import models_list
from .forms import AuthorForm

def all_directories(request):
    context = {
        'all_refs': models_list
    }
    return render(request, 'directory/all_refs.html', context=context)


def all_authors_list_view(request):
    all_authors_list = Author.objects.all()
    context = {
        'authors': all_authors_list
    }
    return render(request, 'directory/author_list.html', context=context)


def author_detailed_view(request, author_id):
    author_obj = Author.objects.get(pk = author_id)
    context = {
        'author': author_obj
    }
    return render(request, 'directory/author_detailed.html', context=context)


def author_create_view(request):
    if request.method == "GET":
        form = AuthorForm()
        return render(request, 'directory/author_create.html', context={'form': form})
    else:
        form = AuthorForm(request.POST)
        if form.is_valid():
            Author.objects.create(author_name = form.cleaned_data['author_name'])
            return redirect('authors')


def author_update_view(request, author_id):
    if request.method == 'POST':
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            new_author_name = form.cleaned_data.get('author_name')
            a = Author.objects.get(pk=author_id)
            print(dir(a))
            a.author_name=new_author_name
            a.save()
            return redirect('authors')
    else:
        author = Author.objects.get(pk=author_id)
        form = AuthorForm(data={"author_name":author.author_name})
    return render(request, 'directory/author_update.html', context={'form':form})


def author_delete_view(request, author_id):
    if request.method == 'POST':
        return redirect('authors')
    else:
        author = Author.objects.get(pk=author_id)
        author.delete()
    return render(request, 'directory/author_delete.html', context={"author": author})