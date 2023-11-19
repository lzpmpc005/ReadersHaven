# ReadersHaven: bookstore management application

## 1 Introduction

This application is designed for bookstore owner to digitalize the book inventory and manage it online. For now, the application has been implemented basic functions like add or delete books.
		
This application is built with Django. However, instead of using libraries built in Django, we break down the functions and write them by ourselves to better understand what's going on and make it easier to modify in the future.

In the future, we expect to implement features like update or delete books in bulk to improve its efficiency.

## 2 How to Install and Run ReadersHaven

* Set up your environment
  * Make sure you are using Windows
Unfortunately, ReadersHaven doesn't support MacOS right now.
  * Install Python3
you can download and install Python3 ['here'](https://www.python.org/downloads/) (latest version recommended).

* Activate local server</b></summary>
  * open terminal and perform:

``` nix
cd path  # path = the path of 'manage.py'
python manage.py runserver
```

* Manage bookstore with browsers
  * open your browser and enjoy ReadersHaven

## 3 Features

* Add book : http://localhost:8000/books/create_book	
* Add author: http://localhost:8000/books/create_author
* Retrieve booklist: http://localhost:8000/books/booklist
* Retrieve booklist sorted by title: http://localhost:8000/books/booklist?order_by=title_asc
* Retrieve booklist sorted by price
  * price ascending: http://localhost:8000/books/booklist?order_by=price_asc
  * price descending: http://localhost:8000/books/booklist?order_by=price_desc
* Filter book by author: http://localhost:8000/books/booklist/filter/name
* Search book by title: http://localhost:8000/books/booklist?title=
* Delete book by id: http://localhost:8000/books/delete/id/
* Update price by id: http://localhost:8000/books/update/

## 4 Project file structure

* ReadersHaven -> main catalog of the project
  * ```settings.py``` -> install built-in and new applications
  * ```urls.py``` -> indicate path of application
* books -> files of the 'books' application
  * ```models.py``` -> define models of the application
  * ```views.py``` -> define functions
  * ```urls.py``` -> indicate paths of functions
* db.sqlite3 -> in-built datebase

## 5 Contribution

If you want to contribute or comment on this project, email lihongtaoix7@gmail.com.
