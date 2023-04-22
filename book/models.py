from django.core.exceptions import ValidationError
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=220)
    author = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
