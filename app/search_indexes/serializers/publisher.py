import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from search_indexes.documents.publisher import PublisherDocument


class PublisherDocumentSerializer(DocumentSerializer):
    """Serializer for the Publisher document."""

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = PublisherDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'name',
            'address',
            'city',
            'state_province',
            'country'
        )
