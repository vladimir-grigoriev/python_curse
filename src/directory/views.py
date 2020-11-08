from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from .models import *
from .admin import models_list
from .models import Author
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
    template_name = "directory/author_CRUDL/authors_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        return context


class AuthorDetailView(DetailView):
    """Выводим детализированную информацию об авторе"""
    model = Author
    template_name = "directory/author_CRUDL/author_detailed.html"
    pk_url_kwarg = 'author_id'


class AuthorCreateView(CreateView):
    """Добавляем нового автора"""
    model = Author
    template_name = "directory/author_CRUDL/author_create.html"
    fields = ['author_name']
    
    def get_success_url(self):
        return reverse('all_authors')


class AuthorUpdateView(UpdateView):
    """Изменяем инофрмацию об авторе"""
    model = Author
    template_name = "directory/author_CRUDL/author_create.html"
    pk_url_kwarg = 'author_id'
    fields = ['author_name']
    success_url = reverse_lazy('all_authors')


class AuthorDeleteView(DeleteView):
    """Удаляем экземпляр автора"""
    model = Author
    template_name = "directory/author_CRUDL/author_delete.html"
    pk_url_kwarg = 'author_id'
    success_url = reverse_lazy('all_authors')


class SeriesListView(ListView):
    """Выводим список всех серий"""
    model = Series
    template_name = "directory/series_CRUDL/series_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["series"] = Series.objects.all()
        return context


class SeriesDetailView(DetailView):
    """Выводим детализированную информацию о серии"""
    model = Series
    template_name = "directory/series_CRUDL/series_detailed.html"
    pk_url_kwarg = 'series_id'


class SeriesCreateView(CreateView):
    """Добавляем новую серию"""
    model = Series
    template_name = "directory/series_CRUDL/series_create.html"
    fields = ['series_name', 'author']
    
    def get_success_url(self):
        return reverse('all_series')


class SeriesUpdateView(UpdateView):
    """Изменяем инофрмацию о серии"""
    model = Series
    template_name = "directory/series_CRUDL/series_create.html"
    pk_url_kwarg = 'series_id'
    fields = ['series_name', 'author']
    success_url = reverse_lazy('all_series')


class SeriesDeleteView(DeleteView):
    """Удаляем экземпляр серии"""
    model = Series
    template_name = "directory/series_CRUDL/series_delete.html"
    pk_url_kwarg = 'series_id'
    success_url = reverse_lazy('all_series')


class GenreListView(ListView):
    """Выводим список всех жанров"""
    model = Genre
    template_name = "directory/genre_CRUDL/genres_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre.objects.all()
        return context


class GenreDetailView(DetailView):
    """Выводим детализированную информацию о жанре"""
    model = Genre
    template_name = "directory/genre_CRUDL/genre_detailed.html"
    pk_url_kwarg = 'genre_id'


class GenreCreateView(CreateView):
    """Добавляем новый жанр"""
    model = Genre
    template_name = "directory/genre_CRUDL/genre_create.html"
    fields = ['genre_name']
    
    def get_success_url(self):
        return reverse('all_genres')


class GenreUpdateView(UpdateView):
    """Изменяем инофрмацию о жанре"""
    model = Genre
    template_name = "directory/genre_CRUDL/genre_create.html"
    pk_url_kwarg = 'genre_id'
    fields = ['genre_name']
    success_url = reverse_lazy('all_genres')


class GenreDeleteView(DeleteView):
    """Удаляем экземпляр жанра"""
    model = Genre
    template_name = "directory/genre_CRUDL/genre_delete.html"
    pk_url_kwarg = 'genre_id'
    success_url = reverse_lazy('all_genres')


class PublisherListView(ListView):
    """Выводим список всех издательств"""
    model = Publisher
    template_name = "directory/publisher_CRUDL/publishers_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publishers"] = Publisher.objects.all()
        return context


class PublisherDetailView(DetailView):
    """Выводим детализированную информацию об издательстве"""
    model = Publisher
    template_name = "directory/publisher_CRUDL/publisher_detailed.html"
    pk_url_kwarg = 'publisher_id'


class PublisherCreateView(CreateView):
    """Добавляем новое издательство"""
    model = Publisher
    template_name = "directory/publisher_CRUDL/publisher_create.html"
    fields = ['publisher_name']
    
    def get_success_url(self):
        return reverse('all_publishers')


class PublisherUpdateView(UpdateView):
    """Изменяем инофрмацию об издательстве"""
    model = Publisher
    template_name = "directory/publisher_CRUDL/publisher_create.html"
    pk_url_kwarg = 'publisher_id'
    fields = ['publisher_name']
    success_url = reverse_lazy('all_publishers')


class PublisherDeleteView(DeleteView):
    """Удаляем экземпляр издательсвта"""
    model = Publisher
    template_name = "directory/publisher_CRUDL/publisher_delete.html"
    pk_url_kwarg = 'publisher_id'
    success_url = reverse_lazy('all_publishers')


class BindingListView(ListView):
    """Выводим список всех типов переплёта"""
    model = Binding
    template_name = "directory/binding_CRUDL/binding_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bindings"] = Binding.objects.all()
        return context


class BindingDetailView(DetailView):
    """Выводим детализированную информацию о переплёте"""
    model = Binding
    template_name = "directory/binding_CRUDL/binding_detailed.html"
    pk_url_kwarg = 'binding_id'


class BindingCreateView(CreateView):
    """Добавляем новый тип переплёта"""
    model = Binding
    template_name = "directory/binding_CRUDL/binding_create.html"
    fields = ['binding_type']
    
    def get_success_url(self):
        return reverse('all_bindings')


class BindingUpdateView(UpdateView):
    """Изменяем инофрмацию о переплёте"""
    model = Binding
    template_name = "directory/binding_CRUDL/binding_create.html"
    pk_url_kwarg = 'binding_id'
    fields = ['binding_type']
    success_url = reverse_lazy('all_bindings')


class BindingDeleteView(DeleteView):
    """Удаляем экземпляр переплёта"""
    model = Binding
    template_name = "directory/binding_CRUDL/binding_delete.html"
    pk_url_kwarg = 'binding_id'
    success_url = reverse_lazy('all_bindings')


class BookFormatListView(ListView):
    """Выводим список всех форматов"""
    model = BookFormat
    template_name = "directory/book_format_CRUDL/book_format_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_formats"] = BookFormat.objects.all()
        return context


class BookFormatDetailView(DetailView):
    """Выводим детализированную информацию форматах"""
    model = BookFormat
    template_name = "directory/book_format_CRUDL/book_format_detailed.html"
    pk_url_kwarg = 'book_format_id'
    

class BookFormatCreateView(CreateView):
    """Добавляем новый формат"""
    model = BookFormat
    template_name = "directory/book_format_CRUDL/book_format_create.html"
    fields = ['book_format']
    
    def get_success_url(self):
        return reverse('all_book_formats')


class BookFormatUpdateView(UpdateView):
    """Изменяем инофрмацию о формате"""
    model = BookFormat
    template_name = "directory/book_format_CRUDL/book_format_create.html"
    pk_url_kwarg = 'book_format_id'
    fields = ['book_format']
    success_url = reverse_lazy('all_book_formats')


class BookFormatDeleteView(DeleteView):
    """Удаляем экземпляр переплёта"""
    model = BookFormat
    template_name = "directory/book_format_CRUDL/book_format_delete.html"
    pk_url_kwarg = 'book_format_id'
    success_url = reverse_lazy('all_book_formats')


class AgeRestrictionListView(ListView):
    """Выводим список всех возрастных ограничений"""
    model = AgeRestriction
    template_name = "directory/age_restrictions_CRUDL/age_restrictions_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["age_restrictions"] = AgeRestriction.objects.all()
        return context


class AgeRestrictionDetailView(DetailView):
    """Выводим детализированную информацию о возрастных ограничениях"""
    model = AgeRestriction
    template_name = "directory/age_restrictions_CRUDL/age_restrictions_detailed.html"
    pk_url_kwarg = 'age_restriction_id'
    

class AgeRestrictionCreateView(CreateView):
    """Добавляем новый тип возрастных ограничений"""
    model = AgeRestriction
    template_name = "directory/age_restrictions_CRUDL/age_restrictions_create.html"
    fields = ['age_restrictions']
    
    def get_success_url(self):
        return reverse('all_age_restrictions')


class AgeRestrictionUpdateView(UpdateView):
    """Изменяем инофрмацию о возрастном ограничении"""
    model = AgeRestriction
    template_name = "directory/age_restrictions_CRUDL/age_restrictions_create.html"
    pk_url_kwarg = 'age_restriction_id'
    fields = ['age_restrictions']
    success_url = reverse_lazy('all_age_restrictions')


class AgeRestrictionDeleteView(DeleteView):
    """Удаляем экземпляр возрастного ограничения"""
    model = AgeRestriction
    template_name = "directory/age_restrictions_CRUDL/age_restrictions_delete.html"
    pk_url_kwarg = 'age_restriction_id'
    success_url = reverse_lazy('all_age_restrictions')
