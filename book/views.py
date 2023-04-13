from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Book
from .serializer import BookSerializer


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIVIew(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
