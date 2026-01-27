from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.book_model import Book
from .models.member_model import Member
from .models.BorrowRecord_model import BorrowRecord



admin.site.register(Book)
admin.site.register(Member)
admin.site.register(BorrowRecord)
