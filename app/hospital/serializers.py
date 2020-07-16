from rest_framework import serializers
from .models.city import City
from .models.province import Province
from .models.hospital import Hospital


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'province']


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['name']


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = [
            'name', 'address', 'max_number_workers', 'city', 'province', 'country'
        ]
