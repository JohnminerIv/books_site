from django.shortcuts import render
from .models import Book


def home(request):
    context = {
        'books': Book.objects.all()
        }
    return render(request, 'books/home.html', context)


def detail(request, book_id):
    context = {'book': Book.objects.get(id=book_id)}
    return render(request, 'books/detail.html', context)
