from django.db import models


class Author(models.Model):
    """docstring for Author."""
    name = models.CharField(max_length=20)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    """docstring for Tag."""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    """docstring for Book."""
    title = models.CharField(max_length=20)
    num_pages = models.IntegerField()
    date_published = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
