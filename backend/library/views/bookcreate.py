from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ..models.book_model import Book


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'isbn', 'quantity']
    template_name = 'library/add_book.html'
    success_url = reverse_lazy('book_list')
