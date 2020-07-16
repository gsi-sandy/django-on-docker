from django.contrib import admin
from hospital.models.city import City
from hospital.models.province import Province


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
