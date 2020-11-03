from django.urls import path, include
from .views import AllDirectoriesView, AuthorsListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView

urlpatterns = [
    path('', AllDirectoriesView.as_view(), name='all_refs'),
    path('authors/', AuthorsListView.as_view(), name='all_authors'),
    path('authors/create/', AuthorCreateView.as_view(), name = 'create_author'),
    path('authors/<int:author_id>/', AuthorDetailView.as_view(), name='author_detailed_info'),
    path('authors/<int:author_id>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:author_id>/delete/', AuthorDeleteView.as_view(), name='author_delete')
]
