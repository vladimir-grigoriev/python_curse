from django.urls import path, include
from .views import all_products_list_view, create_new_product_view, product_detailed_view, product_update_view, product_delete_view

urlpatterns = [
    path('', all_products_list_view, name='all_products_list'),
    path('create/', create_new_product_view, name='create_new_product'),
    path('<int:pk>', product_detailed_view, name='product_detailed'),
    path('<int:pk>/update', product_update_view, name='product_update'),
    path('<int:pk>/delete', product_delete_view, name='delete_product')
]
