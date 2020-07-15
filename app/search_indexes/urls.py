from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from search_indexes.viewset.book import BookDocumentView
from search_indexes.viewset.publisher import PublisherDocumentView

router = DefaultRouter()
books = router.register(r'books', BookDocumentView, basename='bookdocument')
publishers = router.register(r'publishers', PublisherDocumentView, basename='publisherdocument')
urlpatterns = [
    url(r'^', include(router.urls)),
]
