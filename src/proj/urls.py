from django.contrib import admin
from django.urls import path, include
from hello_world.views import HomepageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='homepage'),
    path('directories/', include('directory.urls'), name='hello'),
    path('products/', include('products.urls')),
]
