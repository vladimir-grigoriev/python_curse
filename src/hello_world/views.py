from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from products.models import Book


class HomepageView(TemplateView):
    template_name = "hello_world/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_books"] = Book.objects.order_by('-inclusion_in_catalog_date')[:6]
        context["most_popular"] = Book.objects.order_by('-rating')[:6]
        context['user'] = self.request.user
        return context


