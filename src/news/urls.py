from django.urls import path, include
from rest_framework import routers
from .api_views import PostViewSet

router = routers.DefaultRouter()
router.register(r'', PostViewSet)

app_name = 'news'
urlpatterns = [
    path('', include(router.urls))
]
