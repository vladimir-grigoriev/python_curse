from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
class UserLoginView(LoginView):
    template_name = 'login/login.html'
    success_url = reverse_lazy('hello_world:homepage')


class UserLogoutView(LogoutView):
    template_name = 'login/logout.html'
    