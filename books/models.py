from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.author_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    page_amount = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
