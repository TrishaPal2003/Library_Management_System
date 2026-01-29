
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View
from django.shortcuts import render


from ..models.book_model import Book
from ..models.member_model import Member
from ..models.BorrowRecord_model import BorrowRecord


class IssueBookView(View):
    def get(self, request):
        books = Book.objects.filter(quantity__gt=0)
        members = Member.objects.all()
        return render(request, 'library/issue.html', {
            'books': books,
            'members': members
        })

    def post(self, request):
        book_id = request.POST.get('book')
        member_id = request.POST.get('member')

        book = get_object_or_404(Book, id=book_id)
        member = get_object_or_404(Member, id=member_id)

        if book.quantity > 0:
            BorrowRecord.objects.create(
                book=book,
                member=member
            )
            book.quantity -= 1
            book.save()

        return redirect('borrow_history')







