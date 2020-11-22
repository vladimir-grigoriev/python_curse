from django.urls import path, include
from .views import (ProductsListView, 
                    ProductCreateView, 
                    ProductDetailView, 
                    ProductUpdateView,
                    ProductDeleteView) 

app_name = 'products'
urlpatterns = [
    path('', ProductsListView.as_view(), name='all_products_list'),
    path('create/', ProductCreateView.as_view(), name='create_new_product'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detailed'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='delete_product')
]
