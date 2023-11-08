from django.views import generic
from .models import Book, Author
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'

def book_list(request):
    title = request.GET.get('title')
    books = Book.objects.all()
    if title:
        books = books.filter(title__icontains = title)
    book_array = [{'id': book.id,
                   'title': book.title,
                   'author': book.author.author_name,
                   'price': str(book.price) + "$"
                   } for book in books]
    return JsonResponse(book_array, safe = False)

@csrf_exempt
def create_author(request):
    if request.method == 'POST':
        author_name = json.loads(request.body)["name"]
        author = Author.objects.create(author_name = author_name)
        return JsonResponse({'author_id': author.id})

@csrf_exempt   
def create_book(request):
    if request.method == 'POST':
        json_request = json.loads(request.body)
        title = json_request['title']
        author_id = json_request['author_id']
        price = json_request['price']
        author = Author.objects.get(id = author_id)
        new_book = Book.objects.create(title = title, price = price, author = author)
        return JsonResponse({'book_id': new_book.id})

def filter_books_by_author(request, author_id):
    author = Author.objects.get(id = author_id)
    books = Book.objects.filter(author = author)
    book_array = [{'id': book.id,
                   'title': book.title,
                   'author': book.author.author_name,
                   'price': str(book.price) + "$"
                   } for book in books]
    return JsonResponse(book_array, safe = False)
