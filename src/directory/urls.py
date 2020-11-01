from django.urls import path, include
from .views import all_directories, all_authors_list_view, author_detailed_view, author_create_view, author_update_view, author_delete_view

urlpatterns = [
    path('', all_directories),
    path('authors/', all_authors_list_view, name='authors'),
    path('authors/create/', author_create_view, name = 'author_create_view'),
    path('authors/<int:author_id>/', author_detailed_view, name='author_detailed_view'),
    path('authors/<int:author_id>/update/', author_update_view, name='author_update_view'),
    path('authors/<int:author_id>/delete/', author_delete_view, name='author_delete_view')
]
