from django.contrib import admin
from django.urls import path, include
from hello_world.views import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('directories/', include('directory.urls'), name='hello'),
    path('products/', include('products.urls')),
]
