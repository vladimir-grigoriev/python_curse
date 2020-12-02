from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
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
    

class UserUpdateProfileView(UpdateView):
    model = Profile
    template_name = "user_profile/edit_profile.html"
    fields = [
        'phone',
        'country',
        'city',
        'index',
        'adress',
    ]
    success_url = reverse_lazy('user_profile:profile')
    def get_object(self, *args, **kwargs):
        print(self.request.user.pk)
        obj = Profile.objects.filter(user__pk=self.request.user.pk).first()
        if not obj:
            Profile.objects.create(
                user=User.objects.get(pk=self.request.user.pk)
            )
            obj = Profile.objects.filter(user__pk=self.request.user.pk).first()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = User.objects.get(pk=self.request.user.pk)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = User.objects.get(pk=self.request.user.pk)
        user.first_name = self.request.POST['first_name']
        user.last_name = self.request.POST['last_name']
        user.email = self.request.POST['email']
        user.save()
        return super().post(request, *args, **kwargs)