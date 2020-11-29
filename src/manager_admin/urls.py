from django.urls import path, include
from .views import ManagerAdminView

app_name='manager_admin'
urlpatterns = [
    path('', ManagerAdminView.as_view(), name='dashboard'),
]