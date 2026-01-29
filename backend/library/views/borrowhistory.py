from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView

from ..models.BorrowRecord_model import BorrowRecord



class BorrowHistoryView(ListView):
    model = BorrowRecord
    template_name = 'library/history.html'
    context_object_name = 'records'
