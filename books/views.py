from django.views import generic
from .models import Book, Author
from rest_framework import generics
from .serializers import AuthorSerializer, BookSerializer

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'

class Author_list(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class Book_list(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookFilterByAuthor(generics.ListAPIView):
    serializer_class = BookSerializer
    
    def get_queryset(self):
        author_id = self.kwargs["author_id"]
        return Book.objects.filter(author__id = author_id)

