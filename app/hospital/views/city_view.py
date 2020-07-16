from ..models.city import City
from ..serializers import CitySerializer
from rest_framework import generics


class CityListCreate(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
