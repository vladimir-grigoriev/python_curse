from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .forms import RegistrationUserForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class UserRegistrationView(SuccessMessageMixin, CreateView):
    
    template_name = 'registration/registration.html'
    form_class = RegistrationUserForm
    success_url = reverse_lazy('hello_world:homepage')
    success_message = "Created successfully"

