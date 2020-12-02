
from django.urls import path, include
from .views import ProfileView, HistoryDetailView, OrderDetailView, UserUpdateProfileView

app_name = 'user_profile'
urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('edit/', UserUpdateProfileView.as_view(), name='edit'),
    path('history/', HistoryDetailView.as_view(), name='history'),
    path('history/detailed/', OrderDetailView.as_view(), name='detailed_order')
]