from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View
from django.utils import timezone

from ..models.BorrowRecord_model import BorrowRecord


class ReturnBookView(View):
    def get(self, request, record_id):
        record = get_object_or_404(BorrowRecord, id=record_id, is_returned=False)

        record.is_returned = True
        record.return_date = timezone.now()
        record.save()

        book = record.book
        book.quantity += 1
        book.save()

        return redirect('borrow_history')
