from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views.city_view import CityListCreate, CityDetailUpdateDestroy
from .views.province_view import ProvinceListCreate, ProvinceDetailUpdateDestroy
from .views.hospital_view import HospitalListCreate, HospitalDetailUpdateDestroy


urlpatterns = [
    # Hospitals urls
    path('hospitals/', HospitalListCreate.as_view()),
    path('hospital/<int:pk>/', HospitalDetailUpdateDestroy.as_view()),

    # Cities urls
    path('cities/', CityListCreate.as_view()),
    path('city/<int:pk>/', CityDetailUpdateDestroy.as_view()),

    # Provinces urls
    path('provinces/', ProvinceListCreate.as_view()),
    path('province/<int:pk>/', ProvinceDetailUpdateDestroy.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)