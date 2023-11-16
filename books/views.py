from .models import Book, Author
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re

def book_list(request):
    title = request.GET.get('title')
    order_by = request.GET.get('order_by')
    books = Book.objects.all()
    if title:
        books = books.filter(title__icontains = title)
    if order_by:
        if order_by not in ['price_asc', 'price_desc', 'title_asc', 'title_desc']:
            return JsonResponse({'error': "Incorrect order_by expression"}, status = 400)
        if order_by == 'price_asc':
            books = books.order_by('price')
        if order_by == 'price_desc':
            books = books.order_by('-price')
        if order_by == 'title_asc':
            books = books.order_by('title')
        if order_by == 'title_desc':
            books = books.order_by('-title')

    book_array = [{'id': book.id,
                   'title': book.title,
                   'author': book.author.author_name,
                   'price': str(book.price) + "$"
                   } for book in books]
    if book_array == []:
        return JsonResponse({'error': "Title was not found"}, status = 400)
    return JsonResponse(book_array, safe = False)

@csrf_exempt
def create_author(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode("utf-8"))
            author_name = data.get("name")

            if not author_name or author_name == "":
                return JsonResponse({'error': "Name not specified"}, status = 400)

            if not isinstance(author_name, str):
                return JsonResponse({'error': "Name should be string!"}, status = 400)
            
            sc_number = r'[^\w\s]|\d'
            if re.search(sc_number, author_name):
                return JsonResponse({'error': "Name contains number or special character"}, status = 400)

            exist_author = Author.objects.filter(author_name=author_name).first()
            if exist_author:
                return JsonResponse({'error': "Author is already exist!"}, status = 400)
             
            author = Author.objects.create(author_name = author_name)
            return JsonResponse({'author_id': author.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status = 400)

@csrf_exempt   
def create_book(request):
    if request.method == 'POST':
        try:
            json_request = json.loads(request.body)
            title = json_request.get("title")
            author_id = json_request.get("author_id")
            price = json_request.get("price")

            if not title or not author_id or not price:
                return JsonResponse({'error': "title/author_id/price are required!"}, status = 400)
            if not isinstance(title, str):
                return JsonResponse({'error': "Title should be string"}, status = 400)
            if title == "":
                return JsonResponse({'error': "Book title is empty"}, status = 400)
            
            if not isinstance(author_id, int):
                return JsonResponse({'error': "Author_id should be integer!"}, status = 400)
            if author_id < 0:
                return JsonResponse({'error': "Incorrect author_id"}, status = 400)
            if not isinstance(price, (int, float)):
                return JsonResponse({'error': "Price should be integer or float!"}, status = 400)
            if price < 0:
                return JsonResponse({'error': "Incorrect price"}, status = 400)
            exist_author = Author.objects.filter(id = author_id).first()
            if not exist_author:
                return JsonResponse({'error': "Author is not exist!"}, status = 400)

            new_book = Book.objects.create(title = title, price = price, author = exist_author)
            return JsonResponse({'book_id': new_book.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status = 400)

def filter_books_by_author(request, author_id):
    try:
        author = Author.objects.filter(id = author_id).first()
        if not author:
            return JsonResponse({'error': "Author was not found"}, status = 400)
        books = Book.objects.filter(author = author)
        book_array = [{'id': book.id,
                       'title': book.title,
                       'author': book.author.author_name,
                       'price': str(book.price) + "$"
                       } for book in books]
        return JsonResponse(book_array, safe = False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)

def filter_books_by_author_name(request, author_name):
    try:
        author = Author.objects.filter(author_name = author_name).first()
        if not author:
            return JsonResponse({'error': "Author was not found"}, status = 400)
        books = Book.objects.filter(author = author)
        book_array = [{'id': book.id,
                       'title': book.title,
                       'author': book.author.author_name,
                       'price': str(book.price) + "$"
                       } for book in books]
        return JsonResponse(book_array, safe = False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)

@csrf_exempt    
def delete_book_by_id(request, book_id):
    try:
        book = Book.objects.get(id = book_id)
        if request.method == "DELETE":
            book.delete()
            return JsonResponse({'message': "Book was successfully removed!"})
    except Book.DoesNotExist:
        return JsonResponse({'error': "Book was not found!"}, status = 404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)

@csrf_exempt    
def delete_book_by_title(request):
    try:
        if request.method == "DELETE":
            json_request = json.loads(request.body)
            title = json_request.get("title")
            if not title:
                return JsonResponse({'error': "Title is required field!"}, status = 400)
            book = Book.objects.get(title = title)
            book.delete()
            return JsonResponse({'message': "Book was successfully removed!"})
    except Book.DoesNotExist:
        return JsonResponse({'error': "Book was not found!"}, status = 404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)


