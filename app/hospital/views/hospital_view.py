from ..models.hospital import Hospital
from ..serializers import HospitalSerializer
from rest_framework import generics


class HospitalListCreate(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class HospitalDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
