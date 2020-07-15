from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from search_indexes.viewset.book import BookDocumentView

router = DefaultRouter()
books = router.register(r'books', BookDocumentView, basename='bookdocument')
urlpatterns = [
    url(r'^', include(router.urls)),
]
