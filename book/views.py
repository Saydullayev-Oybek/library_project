from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Book
from .serializer import BookSerializer


class BookListView(viewsets.ViewSet):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)
