from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .forms import BookForm
from .models import Book
from directory.models import Genre
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic import UpdateView, DeleteView


class ProductsListView(ListView):
    model = Book
    template_name = "products/all_products.html"

    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre_pk = self.request.GET.get('genre')
        if genre_pk:
            context['object_list'] = Book.objects.filter(genres__pk=genre_pk)
            context['genre_name'] = Genre.objects.get(pk=genre_pk)
        context['genres'] = Genre.objects.all()
        searching_value = self.request.GET.get('search')
        if searching_value:
            context['searching_value'] = searching_value
            context['object_list'] = Book.objects.filter(name__icontains=searching_value)
        else:
            pass
        
        return context
    

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "products/create_product.html"
    fields = [
        'name',
        'foto',
        'description',
        'price',
        'author',
        'series',
        'genres',
        'year_published',
        'nubmer_of_pages',
        'binding',
        'book_format',
        'book_isbn',
        'weight',
        'age_restrictions',
        'publisher',
        'quantity',
        'book_available',
        'rating',
    ]
    success_url = reverse_lazy('products:all_products_list')
    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ProductDetailView(DetailView):
    model = Book
    template_name = "products/product_detailed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context
    

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = "products/product_update.html"
    fields = [
        'name',
        'foto',
        'description',
        'price',
        'author',
        'series',
        'genres',
        'year_published',
        'nubmer_of_pages',
        'binding',
        'book_format',
        'book_isbn',
        'weight',
        'age_restrictions',
        'publisher',
        'quantity',
        'book_available',
        'rating',
    ]
    success_url = reverse_lazy('products:all_products_list')
    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "products/product_delete.html"
    success_url = reverse_lazy('products:all_products_list')
    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ProductsAdminListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "products/all_products_manager.html"

    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre_pk = self.request.GET.get('genre')
        if genre_pk:
            context['object_list'] = Book.objects.filter(genres__pk=genre_pk)
            context['genre_name'] = Genre.objects.get(pk=genre_pk)
        context['genres'] = Genre.objects.all()
        searching_value = self.request.GET.get('search')
        if searching_value:
            context['searching_value'] = searching_value
            context['object_list'] = Book.objects.filter(name__icontains=searching_value)
        else:
            pass
        return context

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
