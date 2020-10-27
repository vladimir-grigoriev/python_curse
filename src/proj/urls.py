from django.contrib import admin
from django.urls import path, include
from directory.views import get_directory, get_detailed_directory_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_directory),
    path('<int:author_id>/', get_detailed_directory_view),
]
