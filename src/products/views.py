from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import BookForm
from .models import Book
from directory.models import Genre
from django.views.generic import (ListView, 
                                  CreateView, 
                                  DetailView, 
                                  UpdateView, 
                                  DeleteView)


class ProductsListView(ListView):
    model = Book
    paginate_by = 24
    template_name = "products/all_products.html"

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
    

class ProductCreateView(CreateView):
    model = Book
    template_name = "products/create_product.html"
    fields = [
        'name',
        'foto',
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


class ProductDetailView(DetailView):
    model = Book
    template_name = "products/product_detailed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context
    


class ProductUpdateView(UpdateView):
    model = Book
    template_name = "products/product_update.html"
    fields = [
        'name',
        'foto',
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


class ProductDeleteView(DeleteView):
    model = Book
    template_name = "products/product_delete.html"
    success_url = reverse_lazy('products:all_products_list')
