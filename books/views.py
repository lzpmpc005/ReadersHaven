from .models import Book, Author
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re
import pandas as pd
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    # retrieve 'num_per_page' books on each page
    num_per_page = request.GET.get('num_per_page')
    paginator = Paginator(books, num_per_page)
    page_number = request.GET.get('page')
    try:
        page_books = paginator.page(page_number)
    except PageNotAnInteger:
        page_books = paginator.page(1)
    except EmptyPage:
        page_books = paginator.page(paginator.num_pages)
    
    book_array = [{'id': book.id,
                   'title': book.title,
                   'author': book.author.author_name,
                   'price': str(book.price) + "$"
                   } for book in page_books]
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

@csrf_exempt
def update_book(request):
    if request.method == 'POST':
        try:
            json_request = json.loads(request.body)
            book_id = json_request.get("book_id")
            newprice = json_request.get("price")
            if not book_id or not newprice:
                return JsonResponse({'error': "book_id/price are required!"}, status = 400)
            if not isinstance(book_id, int):
                return JsonResponse({'error': "Book_id should be integer!"}, status = 400)
            if not isinstance(newprice, (int, float)):
                return JsonResponse({'error': "Price should be integer or float!"}, status = 400)
            if newprice < 0:
                return JsonResponse({'error': "Incorrect price"}, status = 400)
            Book.objects.get(id=book_id)
            Book.objects.filter(id = book_id).update(price = newprice)
            return JsonResponse({'message': "Price successfully updated!"})
        except Book.DoesNotExist:
            return JsonResponse({'error': "Book was not found!"}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status = 400)


@csrf_exempt
def bulk_create_book(request):
    if request.method == 'POST':
        try:
            json_request = json.loads(request.body)
            chunk_size = json_request.get('chunk_size')
            csv_file = json_request.get('csv_file')
            for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
                authors = [Author(author_name=author) for author in set(chunk['author'])]
                Author.objects.bulk_create(authors)
                books = []
                for index, row in chunk.iterrows():
                    author = Author.objects.filter(author_name=row['author']).first()
                    books.append(Book(title=row['title'], author=author, price=row['price']))
                Book.objects.bulk_create(books)
            return JsonResponse({'Books': "Added successfully!"})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def bulk_delete_books(request):
    if request.method == 'DELETE':
        try:
            json_request = json.loads(request.body)
            book_ids = json_request.get('book_ids')
            if not book_ids:
                return JsonResponse({'error': "Book identificators are required fields!"}, status = 400)
            Book.objects.filter(id__in = book_ids).delete()
            return JsonResponse({'message': "Books were successfully removed!"})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
