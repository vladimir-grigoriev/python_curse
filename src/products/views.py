from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookForm
from .models import Book


def all_products_list_view(request):
    all_products = Book.objects.all()
    return render(request, 'products/all_products.html', context={'books':all_products})

def create_new_product_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        form.save()
        return redirect('all_products_list')
    else:
        form = BookForm()
        return render(request, 'products/create_product.html', context={'form': form})

def product_detailed_view(request, pk):
    selected_product = Book.objects.get(pk=pk)
    return render(request, 'products/product_detailed.html', context={'book': selected_product})

def product_update_view(request, pk):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_products_list')
    else:
        book = Book.objects.get(pk=pk)
        form = BookForm(instance=book)
        return render(request, 'products/product_update.html', context={'form': form})

def product_delete_view(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('all_products_list')
    context = {'item': book}
    return render(request, 'products/product_delete.html', context)