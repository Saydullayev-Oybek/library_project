from django.urls import path
from .views import BookListView

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('', BookListView, basename='book-list')

urlpatterns = router.urls
