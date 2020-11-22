from django.urls import path, include
from .views import UserRegistrationView

app_name = 'registration'
urlpatterns = [
    path('', UserRegistrationView.as_view(), name='login'),
]
