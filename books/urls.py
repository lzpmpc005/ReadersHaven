from django.urls import path
from . import views
from .views import book_list, create_author, create_book, filter_books_by_author

urlpatterns = [
    path('', views.BookListView.as_view(), name = 'books-book_list'),
    path('booklist/', book_list, name = 'BookList'),
    path('create_author', create_author, name = 'Create_Author'),
    path('create_book', create_book, name = 'Create_Book'),
    path('booklist/filter/<int:author_id>/', filter_books_by_author, name = 'Filter_By_Author')
]