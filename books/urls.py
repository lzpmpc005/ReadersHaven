from django.urls import path
from .views import AuthorCreation, BookCreation

urlpatterns = [
    path('authors', AuthorCreation.as_view(), name = 'AuthorList'),
    path('books', BookCreation.as_view(), name = 'BookList')
]