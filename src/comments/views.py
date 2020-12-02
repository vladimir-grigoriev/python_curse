from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models import Comment
from products.models import Book
from .forms import CommentForm
from directory.models import Genre

User = get_user_model()
# Create your views here.

# class CommentCreateView(CreateView):
#     model = Comment
#     template_name = "comments/create.html"
#     success_url = reverse_lazy('products:all_products_list')
#     fields = ['comment']

def comment_create_view(request):
    form = CommentForm()
    book_id = request.GET['book']
    book = Book.objects.get(pk=book_id)
    user_pk = request.user.pk
    user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        Comment.objects.create(product=book, user=user, comment=request.POST.get('comment'))
        return redirect('products:product_detailed', pk=book_id)
    else:
        print('goodbye')
    return render(
        request, 
        'comments/create.html', 
        context={'form':form, 'book':book, 'user':user, 'genres': Genre.objects.all()})
