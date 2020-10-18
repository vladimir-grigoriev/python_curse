from django.contrib import admin
from django.urls import path, include
from hello_world.views import hello_world
from directory.views import get_directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('directory/', include('directory.urls')),
]
