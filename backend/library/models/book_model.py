from django.db import models


# --------------------------
# Book Model
# --------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    quantity = models.PositiveIntegerField(default=1)  # No negative quantities

    def __str__(self):
        return f"{self.title} by {self.author}"