from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from orders.models import Order
from directory.admin import models_list
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin


class ManagerAdminView(LoginRequiredMixin, ListView):
    template_name = "manager_admin/dashboard.html"
    model = Order
    paginate_by = 10
    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dirs"] = models_list
        return context
    

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "manager_admin/order.html"
    
    def get_object(self, queryset=None):
        order_pk = self.request.GET.get('order')
        obj = Order.objects.get(pk=order_pk)
        return obj
    
    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = "manager_admin/edit_order.html"
    success_url = reverse_lazy('manager_admin:dashboard')
    fields = [
        'status',
        'fio',
        'phone',
        'email',
        'delivery',
        'already_paid'
    ]

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "manager_admin/delete_order.html"
    success_url = reverse_lazy('manager_admin:dashboard')

    login_url = reverse_lazy('login:login')
    permission_denied_message = 'Not today'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

# Create your views here.
