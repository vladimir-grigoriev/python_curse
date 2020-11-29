
from django.urls import path, include
from .views import ProfileView, HistoryDetailView, OrderDetailView

app_name = 'user_profile'
urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('history/', HistoryDetailView.as_view(), name='history'),
    path('history/detailed/', OrderDetailView.as_view(), name='detailed_order')
]