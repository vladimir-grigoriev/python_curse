from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from .models import *
from .admin import models_list
from .models import Author
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class AllDirectoriesView(LoginRequiredMixin, TemplateView):
    """Выводим список всех справочников"""
    template_name = "directory/all_refs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_refs"] = models_list
        return context
    
    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AuthorsListView(LoginRequiredMixin, ListView):
    """Выводим список всех авторов"""
    model = Author
    template_name = "directory/author_CRUDL/authors_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        return context

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AuthorDetailView(LoginRequiredMixin, DetailView):
    """Выводим детализированную информацию об авторе"""
    model = Author
    template_name = "directory/author_CRUDL/author_detailed.html"
    pk_url_kwarg = 'author_id'

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AuthorCreateView(LoginRequiredMixin, CreateView):
    """Добавляем нового автора"""
    model = Author
    template_name = "directory/author_CRUDL/author_create.html"
    fields = ['author_name']
    
    def get_success_url(self):
        return reverse('all_authors')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    """Изменяем инофрмацию об авторе"""
    model = Author
    template_name = "directory/author_CRUDL/author_create.html"
    pk_url_kwarg = 'author_id'
    fields = ['author_name']
    success_url = reverse_lazy('all_authors')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляем экземпляр автора"""
    model = Author
    template_name = "directory/author_CRUDL/author_delete.html"
    pk_url_kwarg = 'author_id'
    success_url = reverse_lazy('all_authors')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SeriesListView(LoginRequiredMixin, ListView):
    """Выводим список всех серий"""
    model = Series
    template_name = "directory/series_CRUDL/series_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["series"] = Series.objects.all()
        return context
    
    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SeriesDetailView(LoginRequiredMixin, DetailView):
    """Выводим детализированную информацию о серии"""
    model = Series
    template_name = "directory/series_CRUDL/series_detailed.html"
    pk_url_kwarg = 'series_id'

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SeriesCreateView(LoginRequiredMixin, CreateView):
    """Добавляем новую серию"""
    model = Series
    template_name = "directory/series_CRUDL/series_create.html"
    fields = ['series_name', 'author']
    
    def get_success_url(self):
        return reverse('all_series')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SeriesUpdateView(LoginRequiredMixin, UpdateView):
    """Изменяем инофрмацию о серии"""
    model = Series
    template_name = "directory/series_CRUDL/series_create.html"
    pk_url_kwarg = 'series_id'
    fields = ['series_name', 'author']
    success_url = reverse_lazy('all_series')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class SeriesDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляем экземпляр серии"""
    model = Series
    template_name = "directory/series_CRUDL/series_delete.html"
    pk_url_kwarg = 'series_id'
    success_url = reverse_lazy('all_series')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class GenreListView(LoginRequiredMixin, ListView):
    """Выводим список всех жанров"""
    model = Genre
    template_name = "directory/genre_CRUDL/genres_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre.objects.all()
        return context

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class GenreDetailView(LoginRequiredMixin, DetailView):
    """Выводим детализированную информацию о жанре"""
    model = Genre
    template_name = "directory/genre_CRUDL/genre_detailed.html"
    pk_url_kwarg = 'genre_id'

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class GenreCreateView(LoginRequiredMixin, CreateView):
    """Добавляем новый жанр"""
    model = Genre
    template_name = "directory/genre_CRUDL/genre_create.html"
    fields = ['genre_name']
    
    def get_success_url(self):
        return reverse('all_genres')
    
    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class GenreUpdateView(LoginRequiredMixin, UpdateView):
    """Изменяем инофрмацию о жанре"""
    model = Genre
    template_name = "directory/genre_CRUDL/genre_create.html"
    pk_url_kwarg = 'genre_id'
    fields = ['genre_name']
    success_url = reverse_lazy('all_genres')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class GenreDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляем экземпляр жанра"""
    model = Genre
    template_name = "directory/genre_CRUDL/genre_delete.html"
    pk_url_kwarg = 'genre_id'
    success_url = reverse_lazy('all_genres')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class PublisherListView(LoginRequiredMixin, ListView):
    """Выводим список всех издательств"""
    model = Publisher
    template_name = "directory/publisher_CRUDL/publishers_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publishers"] = Publisher.objects.all()
        return context

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class PublisherDetailView(LoginRequiredMixin, DetailView):
    """Выводим детализированную информацию об издательстве"""
    model = Publisher
    template_name = "directory/publisher_CRUDL/publisher_detailed.html"
    pk_url_kwarg = 'publisher_id'

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class PublisherCreateView(LoginRequiredMixin, CreateView):
    """Добавляем новое издательство"""
    model = Publisher
    template_name = "directory/publisher_CRUDL/publisher_create.html"
    fields = ['publisher_name']
    
    def get_success_url(self):
        return reverse('all_publishers')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class PublisherUpdateView(LoginRequiredMixin, UpdateView):
    """Изменяем инофрмацию об издательстве"""
    model = Publisher
    template_name = "directory/publisher_CRUDL/publisher_create.html"
    pk_url_kwarg = 'publisher_id'
    fields = ['publisher_name']
    success_url = reverse_lazy('all_publishers')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class PublisherDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляем экземпляр издательсвта"""
    model = Publisher
    template_name = "directory/publisher_CRUDL/publisher_delete.html"
    pk_url_kwarg = 'publisher_id'
    success_url = reverse_lazy('all_publishers')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BindingListView(LoginRequiredMixin, ListView):
    """Выводим список всех типов переплёта"""
    model = Binding
    template_name = "directory/binding_CRUDL/binding_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bindings"] = Binding.objects.all()
        return context
    
    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BindingDetailView(LoginRequiredMixin, DetailView):
    """Выводим детализированную информацию о переплёте"""
    model = Binding
    template_name = "directory/binding_CRUDL/binding_detailed.html"
    pk_url_kwarg = 'binding_id'

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BindingCreateView(LoginRequiredMixin, CreateView):
    """Добавляем новый тип переплёта"""
    model = Binding
    template_name = "directory/binding_CRUDL/binding_create.html"
    fields = ['binding_type']
    
    def get_success_url(self):
        return reverse('all_bindings')
    
    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BindingUpdateView(LoginRequiredMixin, UpdateView):
    """Изменяем инофрмацию о переплёте"""
    model = Binding
    template_name = "directory/binding_CRUDL/binding_create.html"
    pk_url_kwarg = 'binding_id'
    fields = ['binding_type']
    success_url = reverse_lazy('all_bindings')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BindingDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляем экземпляр переплёта"""
    model = Binding
    template_name = "directory/binding_CRUDL/binding_delete.html"
    pk_url_kwarg = 'binding_id'
    success_url = reverse_lazy('all_bindings')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BookFormatListView(LoginRequiredMixin, ListView):
    """Выводим список всех форматов"""
    model = BookFormat
    template_name = "directory/book_format_CRUDL/book_format_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_formats"] = BookFormat.objects.all()
        return context
    
    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BookFormatDetailView(LoginRequiredMixin, DetailView):
    """Выводим детализированную информацию форматах"""
    model = BookFormat
    template_name = "directory/book_format_CRUDL/book_format_detailed.html"
    pk_url_kwarg = 'book_format_id'
    
    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BookFormatCreateView(LoginRequiredMixin, CreateView):
    """Добавляем новый формат"""
    model = BookFormat
    template_name = "directory/book_format_CRUDL/book_format_create.html"
    fields = ['book_format']
    
    def get_success_url(self):
        return reverse('all_book_formats')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BookFormatUpdateView(LoginRequiredMixin, UpdateView):
    """Изменяем инофрмацию о формате"""
    model = BookFormat
    template_name = "directory/book_format_CRUDL/book_format_create.html"
    pk_url_kwarg = 'book_format_id'
    fields = ['book_format']
    success_url = reverse_lazy('all_book_formats')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BookFormatDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляем экземпляр переплёта"""
    model = BookFormat
    template_name = "directory/book_format_CRUDL/book_format_delete.html"
    pk_url_kwarg = 'book_format_id'
    success_url = reverse_lazy('all_book_formats')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AgeRestrictionListView(LoginRequiredMixin, ListView):
    """Выводим список всех возрастных ограничений"""
    model = AgeRestriction
    template_name = "directory/age_restrictions_CRUDL/age_restrictions_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["age_restrictions"] = AgeRestriction.objects.all()
        return context

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AgeRestrictionDetailView(LoginRequiredMixin, DetailView):
    """Выводим детализированную информацию о возрастных ограничениях"""
    model = AgeRestriction
    template_name = "directory/age_restrictions_CRUDL/age_restrictions_detailed.html"
    pk_url_kwarg = 'age_restriction_id'

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    

class AgeRestrictionCreateView(LoginRequiredMixin, CreateView):
    """Добавляем новый тип возрастных ограничений"""
    model = AgeRestriction
    template_name = "directory/age_restrictions_CRUDL/age_restrictions_create.html"
    fields = ['age_restrictions']
    
    def get_success_url(self):
        return reverse('all_age_restrictions')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AgeRestrictionUpdateView(LoginRequiredMixin, UpdateView):
    """Изменяем инофрмацию о возрастном ограничении"""
    model = AgeRestriction
    template_name = "directory/age_restrictions_CRUDL/age_restrictions_create.html"
    pk_url_kwarg = 'age_restriction_id'
    fields = ['age_restrictions']
    success_url = reverse_lazy('all_age_restrictions')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AgeRestrictionDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляем экземпляр возрастного ограничения"""
    model = AgeRestriction
    template_name = "directory/age_restrictions_CRUDL/age_restrictions_delete.html"
    pk_url_kwarg = 'age_restriction_id'
    success_url = reverse_lazy('all_age_restrictions')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
