## Start Local server by
'''python manage.py runserver'''

# Test with Postman
 
## Add books: Post http://localhost:8000/books/create_book

## Filter by author id or name: Get http://localhost:8000/books/booklist/filter/id or name

## Retrieve booklist: Get http://localhost:8000/books/booklist

## Search by title: Get http://localhost:8000/books/booklist?title=

## Sort by title: Get http://localhost:8000/books/booklist/atitle

## Sort by price descending: Get http://localhost:8000/books/booklist/deprice

## Sort by price ascending: Get http://localhost:8000/books/booklist/aprice
