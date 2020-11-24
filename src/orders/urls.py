from django.urls import path, include
from .views import CartView, DeleteBookInCartView, CartUpdateView, CreateOrderView, HistoryDetailView

app_name = 'orders'
urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('delete-book-in-cart/<int:pk>', DeleteBookInCartView.as_view(), name='book_in_cart-del'),
    path('update-cart/', CartUpdateView.as_view(), name='update'),
    path('order/<int:pk>', CreateOrderView.as_view()),
    path('cart/history/', HistoryDetailView.as_view(), name='history')
]