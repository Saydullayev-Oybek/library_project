from django.urls import path
from .views import BookAPIViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookAPIViewSet, basename='books')

urlpatterns = router.urls

# from .views import (
#     BookListAPIView,
#     BookDetailAPIVIew,
#     BookDeleteView,
#     BookUpdateView,
#     BookCreateView,
#     BookListCreateView,
#     BookDetailUpdateDeleteView,
# )
#
# urlpatterns = [
#     path('', BookListAPIView.as_view(),),
#     path('book/create/', BookCreateView.as_view()),
#     path('book-list/create/', BookListCreateView.as_view()),
#     path('<int:pk>/', BookDetailAPIVIew.as_view(),),
#     path('<int:pk>/update/', BookUpdateView.as_view(),),
#     path('<int:pk>/delete/', BookDeleteView.as_view(),),
#     path('<int:pk>/book-update-delete/', BookDetailUpdateDeleteView.as_view()),
# ]