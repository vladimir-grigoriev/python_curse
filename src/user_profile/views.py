from django.shortcuts import render
from django.views.generic import DetailView
from .models import Profile
from orders.models import Order
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileView(DetailView):
    model = Profile
    template_name = "user_profile/profile.html"

    def get_object(self, *args, **kwargs):
        user_id = self.request.user.pk
        obj = User.objects.filter(pk=user_id).first()
        return obj


class HistoryDetailView(DetailView):
    model = User
    template_name = 'user_profile/history.html'
    def get_object(self, *args, **kwargs):
        obj = User.objects.get(username=self.request.user)
        return obj


class OrderDetailView(DetailView):
    model = User
    template_name = "user_profile/detailed_order.html"
    

    def get_object(self, *args, **kwargs):
        obj = User.objects.get(username=self.request.user)
        return obj
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # сделать проверку, принадлежит ли заказ этому пользователю
        context["order"] = Order.objects.get(pk=self.request.GET.get('order'))
        return context
    

