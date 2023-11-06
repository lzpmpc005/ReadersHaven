from django.urls import path
from . import views
from .views import Author_list, Book_list, BookFilterByAuthor

urlpatterns = [
    path('', views.BookListView.as_view(), name = 'books-book_list'),
    path('booklist', Book_list.as_view(), name = 'BookList'),
    path('authorlist', Author_list.as_view(), name = 'AuthorList'),
    path('booklist/filter/<int:author_id>/', BookFilterByAuthor.as_view(), name = 'Filter-by-Author')
]