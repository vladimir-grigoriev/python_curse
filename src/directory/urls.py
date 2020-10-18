from django.urls import path, include
from .views import get_directory

urlpatterns = [
    path('', get_directory),
]
