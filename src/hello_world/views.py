import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from products.models import Book
from directory.models import Genre


class HomepageView(TemplateView):
    template_name = "hello_world/index.html"

    def get_current_curse(self):
        result = requests.get('https://www.nbrb.by/api/exrates/rates/145')
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_books"] = Book.objects.order_by('-inclusion_in_catalog_date')[:6]
        context["most_popular"] = Book.objects.order_by('-rating')[:6]
        context['user'] = self.request.user
        context['genres'] = Genre.objects.all()
        try:
            page = self.get_current_curse()
            rate = page.json()['Cur_OfficialRate']
            context['rate'] = rate
            
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        return context


