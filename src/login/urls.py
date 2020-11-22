from django.urls import path, include
from .views import UserLoginView


app_name = 'login'
urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
]
