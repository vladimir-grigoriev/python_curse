from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from orders.models import Order
from directory.admin import models_list
from django.core.paginator import Paginator


class ManagerAdminView(ListView):
    template_name = "manager_admin/dashboard.html"
    model = Order
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dirs"] = models_list
        return context
    


# Create your views here.
