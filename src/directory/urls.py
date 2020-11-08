from django.urls import path, include
from .views import AllDirectoriesView, AuthorsListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView
from .views import SeriesListView, SeriesDetailView, SeriesCreateView, SeriesUpdateView, SeriesDeleteView
from .views import GenreListView, GenreDetailView, GenreCreateView, GenreUpdateView, GenreDeleteView
from .views import PublisherListView, PublisherDetailView, PublisherCreateView, PublisherUpdateView, PublisherDeleteView
from .views import BindingListView, BindingDetailView, BindingCreateView, BindingUpdateView, BindingDeleteView
from .views import BookFormatListView, BookFormatDetailView, BookFormatCreateView, BookFormatUpdateView, BookFormatDeleteView
from .views import AgeRestrictionListView, AgeRestrictionDetailView, AgeRestrictionCreateView, AgeRestrictionUpdateView, AgeRestrictionDeleteView


urlpatterns = [
    path('', AllDirectoriesView.as_view(), name='all_refs'),
    path('authors/', AuthorsListView.as_view(), name='all_authors'),
    path('authors/create/', AuthorCreateView.as_view(), name = 'create_author'),
    path('authors/<int:author_id>/', AuthorDetailView.as_view(), name='author_detailed_info'),
    path('authors/<int:author_id>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:author_id>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    path('series/', SeriesListView.as_view(), name='all_series'),
    path('series/create/', SeriesCreateView.as_view(), name='create_series'),
    path('series/<int:series_id>/', SeriesDetailView.as_view(), name='series_detailed_info'),
    path('series/<int:series_id>/update/', SeriesUpdateView.as_view(), name='series_update'),
    path('series/<int:series_id>/delete/', SeriesDeleteView.as_view(), name='series_delete'),
    path('genres/', GenreListView.as_view(), name='all_genres'),
    path('genres/create/', GenreCreateView.as_view(), name = 'create_genre'),
    path('genres/<int:genre_id>/', GenreDetailView.as_view(), name='genre_detailed_info'),
    path('genres/<int:genre_id>/update/', GenreUpdateView.as_view(), name='genre_update'),
    path('genres/<int:genre_id>/delete/', GenreDeleteView.as_view(), name='genre_delete'),
    path('publishers/', PublisherListView.as_view(), name='all_publishers'),
    path('publishers/create/', PublisherCreateView.as_view(), name = 'create_publisher'),
    path('publishers/<int:publisher_id>/', PublisherDetailView.as_view(), name='publisher_detailed_info'),
    path('publishers/<int:publisher_id>/update/', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publishers/<int:publisher_id>/delete/', PublisherDeleteView.as_view(), name='publisher_delete'),
    path('binding/', BindingListView.as_view(), name='all_bindings'),
    path('binding/create/', BindingCreateView.as_view(), name = 'create_binding'),
    path('binding/<int:binding_id>/', BindingDetailView.as_view(), name='binding_detailed_info'),
    path('binding/<int:binding_id>/update/', BindingUpdateView.as_view(), name='binding_update'),
    path('binding/<int:binding_id>/delete/', BindingDeleteView.as_view(), name='binding_delete'),
    path('book_formats/', BookFormatListView.as_view(), name='all_book_formats'),
    path('book_formats/create/', BookFormatCreateView.as_view(), name = 'create_book_format'),
    path('book_formats/<int:book_format_id>/', BookFormatDetailView.as_view(), name='book_format_detailed_info'),
    path('book_formats/<int:book_format_id>/update/', BookFormatUpdateView.as_view(), name='book_format_update'),
    path('book_formats/<int:book_format_id>/delete/', BookFormatDeleteView.as_view(), name='book_format_delete'),
    path('age_restrictions/', AgeRestrictionListView.as_view(), name='all_age_restrictions'),
    path('age_restrictions/create/', AgeRestrictionCreateView.as_view(), name = 'create_age_restriction'),
    path('age_restrictions/<int:age_restriction_id>/', AgeRestrictionDetailView.as_view(), name='age_restriction_detailed_info'),
    path('age_restrictions/<int:age_restriction_id>/update/', AgeRestrictionUpdateView.as_view(), name='age_restriction_update'),
    path('age_restrictions/<int:age_restriction_id>/delete/', AgeRestrictionDeleteView.as_view(), name='age_restriction_delete'),
]
