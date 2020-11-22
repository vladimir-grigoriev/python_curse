from django.contrib import admin
from .views import HomepageView
from django.urls import path, include

app_name = 'hello_world'
urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('directories/', include('directory.urls'), name='hello'),
]
