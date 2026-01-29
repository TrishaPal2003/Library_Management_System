from django.urls import path
from .views.bookcreate import BookCreateView
from .views.booklist import BookListView
from .views.borrowhistory import BorrowHistoryView
from .views.issuebook import IssueBookView
from .views.membercreate import MemberCreateView
from .views.memberlist import MemberListView
from .views.returnbook import ReturnBookView
from .views.home import home

urlpatterns = [
    path('', home, name='home'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add/', BookCreateView.as_view(), name='add_book'),

    path('members/', MemberListView.as_view(), name='member_list'),
    path('members/add/', MemberCreateView.as_view(), name='add_member'),

    path('issue/', IssueBookView.as_view(), name='issue_book'),
    path('return/<int:record_id>/', ReturnBookView.as_view(), name='return_book'),

    path('history/', BorrowHistoryView.as_view(), name='borrow_history'),
]
