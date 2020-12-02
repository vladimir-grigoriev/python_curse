from django.shortcuts import render, reverse
from django.views.generic import CreateView
from django.contrib.auth.models import Group
from .forms import RegistrationUserForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from user_profile.models import Profile

User = get_user_model()

class UserRegistrationView(SuccessMessageMixin, CreateView):
    
    template_name = 'registration/registration.html'
    form_class = RegistrationUserForm
    success_url = reverse_lazy('hello_world:homepage')
    success_message = "Created successfully"
    
    def form_valid(self, form):
        valid = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        group = Group.objects.get(name='Users')
        self.request.user.groups.add(group)

        return valid
