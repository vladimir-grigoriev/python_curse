from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *
from .admin import models_list
from .models import Author
from .forms import AuthorForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

class AllDirectoriesView(TemplateView):
    """Выводим список всех справочников"""
    template_name = "directory/all_refs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_refs"] = models_list
        return context
    

class AuthorsListView(ListView):
    """Выводим список всех авторов"""
    model = Author
    template_name = "directory/authors_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        return context


class AuthorDetailView(DetailView):
    """Выводим детализированную информацию об авторе"""
    model = Author
    template_name = "directory/author_detailed.html"
    pk_url_kwarg = 'author_id'


class AuthorCreateView(CreateView):
    """Добавляем нового автора"""
    model = Author
    template_name = "directory/author_create.html"
    fields = ['author_name']
    
    def get_success_url(self):
        return reverse('all_authors')


class AuthorUpdateView(UpdateView):
    """Изменяем инофрмацию об авторе"""
    model = Author
    template_name = "directory/author_create.html"
    pk_url_kwarg = 'author_id'
    fields = ['author_name']
    success_url = reverse_lazy('all_authors')


class AuthorDeleteView(DeleteView):
    """Удаляем экземпляр автора"""
    model = Author
    template_name = "directory/author_delete.html"
    pk_url_kwarg = 'author_id'
    success_url = reverse_lazy('all_authors')