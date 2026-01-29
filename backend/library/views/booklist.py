from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView

from ..models.book_model import Book



class BookListView(ListView):
    model = Book
    template_name = 'library/books.html'
    context_object_name = 'books'
