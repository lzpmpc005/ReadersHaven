from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer

# create new book

class AuthorCreation(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookCreation(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
