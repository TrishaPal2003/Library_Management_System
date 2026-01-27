from django.db import models


# --------------------------
# Member Model
# --------------------------
class Member(models.Model):
    student_id = models.CharField(max_length=20, unique=True)  
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.student_id} - {self.name}"
