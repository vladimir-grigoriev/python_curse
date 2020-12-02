from django.urls import path, include
from .views import ManagerAdminView, OrderDetailView, OrderUpdateView, OrderDeleteView

app_name='manager_admin'
urlpatterns = [
    path('', ManagerAdminView.as_view(), name='dashboard'),
    path('order/', OrderDetailView.as_view(), name='order'),
    path('order/<int:pk>/', OrderUpdateView.as_view(), name='edit'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='delete')
]