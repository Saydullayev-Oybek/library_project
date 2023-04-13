from django.urls import path
from .views import BookListAPIView, BookDetailAPIVIew, BookDeleteView, BookUpdateView

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailAPIVIew.as_view(), name='book-detail'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]