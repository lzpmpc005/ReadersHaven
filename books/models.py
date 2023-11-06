from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.author_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return self.title
