from django.urls import path
from .views import book_list, create_author, create_book, filter_books_by_author,filter_books_by_author_name

urlpatterns = [
    path('booklist/', book_list, name = 'BookList'),
    path('create_author', create_author, name = 'Create_Author'),
    path('create_book', create_book, name = 'Create_Book'),
    path('booklist/filter/<int:author_id>/', filter_books_by_author, name = 'Filter_By_Author'),
    path('booklist/filter/<author_name>/', filter_books_by_author_name, name = 'Filter_By_Author_name'),
]