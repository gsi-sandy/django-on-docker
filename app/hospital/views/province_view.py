from ..models.province import Province
from ..serializers import ProvinceSerializer
from rest_framework import generics


class ProvinceListCreate(generics.ListCreateAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class ProvinceDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
