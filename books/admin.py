from django.contrib import admin
from .models import Book, Author

admin.site.register(Author)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    list_filter = ('author', 'title', 'price')

admin.site.register(Book, BookAdmin)
