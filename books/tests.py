from django.test import TestCase
from .models import Author, Book


# Create your tests here.
class AuthorModeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(author_name='Leo Tolstoy')

    def test_author_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("author_name").verbose_name
        self.assertEqual(field_label, "author name")


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # author = Author.objects.get(id=1)
        Author.objects.create(author_name='Leo Tolstoy')
        Book.objects.create(title='War and Peace', author=Author.objects.get(), price='39.9')

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_author_name_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_price_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_author_name_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('author').max_length
        self.assertEqual(max_length, None)

    def test_price_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('price').max_length
        self.assertEqual(max_length, 10)

    def test_object_name_is_title_comma_author_comma_price(self):
        book = Book.objects.get(id=1)
        expected_object_name = book.title
        self.assertEqual(str(book), expected_object_name)

