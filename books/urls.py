from django.urls import path
from .views import (book_list, create_author, create_book, filter_books_by_author,filter_books_by_author_name,
                    sort_books_by_price_ascending,sort_books_by_price_descending,sort_books_by_title)

urlpatterns = [
    path('booklist/', book_list, name = 'BookList'),
    path('create_author', create_author, name = 'Create_Author'),
    path('create_book', create_book, name = 'Create_Book'),
    path('booklist/filter/<int:author_id>/', filter_books_by_author, name = 'Filter_By_Author'),
    path('booklist/filter/<author_name>/', filter_books_by_author_name, name = 'Filter_By_Author_name'),
    path('booklist/aprice/', sort_books_by_price_ascending, name = 'sort_books_by_price_ascending'),
    path('booklist/deprice/', sort_books_by_price_descending, name='sort_books_by_price_descending'),
    path('booklist/atitle/', sort_books_by_title, name = 'sort_books_by_title'),
]