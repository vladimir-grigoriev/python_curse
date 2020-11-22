from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import BookForm
from .models import Book
from django.views.generic import (ListView, 
                                  CreateView, 
                                  DetailView, 
                                  UpdateView, 
                                  DeleteView)


class ProductsListView(ListView):
    model = Book
    template_name = "products/all_products.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.all()
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
