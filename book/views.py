from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Book
from .serializer import BookSerializer

class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# class BookListAPIView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookListAPIView(APIView):
#
#     def get(self, request):
#         books = Book.objects.all()
#         serializer_data = BookSerializer(books, many=True).data
#         data = {
#             'status': f"returned {len(books)}",
#             'data': serializer_data,
#         }
#
#         return Response(data)
#
# # class BookDetailAPIVIew(RetrieveAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer
#
# class BookDetailAPIVIew(APIView):
#
#         def get(self, request, pk):
#             try:
#                 book = Book.objects.get(id=pk)
#                 serializer = BookSerializer(book)
#
#                 data = {
#                     'serializer': serializer.data
#                 }
#                 return Response(data)
#             except:
#                 return Response({
#                     'status': 'Doest not exists',
#                     'message': 'Book not fount',
#                 }, status=status.HTTP_404_NOT_FOUND)
#
#
# # class BookDeleteView(DestroyAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer
#
# class BookDeleteView(APIView):
#
#     def delete(self, request, pk):
#         try:
#             book = Book.objects.get(id=pk)
#             book.delete()
#             return Response({
#                 'status': True,
#                 'message': 'Successfully deleted'
#             }, status=status.HTTP_200_OK)
#         except Exception:
#             return Response({
#                 'status': False,
#                 'message': 'Book is not found'
#             }, status=status.HTTP_400_BAD_REQUEST)
#
# # class BookUpdateView(UpdateAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer
#
# class  BookUpdateView(APIView):
#
#     def patch(self, request, pk):
#         book = Book.objects.get(id=pk)
#         serializer = BookSerializer(instance=book, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'serializer': serializer.data,
#                 'status': status.HTTP_200_OK,
#                 'message': 'Successfully updated'
#             }
#             return Response(data)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # class BookCreateView(CreateAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer
#
# class BookCreateView(APIView):
#
#     def put(self, request):
#         data = request.data
#         serializer = BookSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': status.HTTP_200_OK,
#                 'serializer': serializer.data
#             }
#
#             return Response(data)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BookListCreateView(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
