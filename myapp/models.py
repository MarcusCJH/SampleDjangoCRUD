from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Adding a unique constraint
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title