import json
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from six import python_2_unicode_compatible
from ..models.city import City
from ..models.province import Province

# Enum for city
CUBA_COUNTRY = 'cuba'
UNITED_STATES_COUNTRY = 'united_states_of_america'
COUNTRY_ENUM_CHOICE = (
    (CUBA_COUNTRY, "CUBA"),
    (UNITED_STATES_COUNTRY, "United States of America"),
)
DEFAULT_COUNTRY = CUBA_COUNTRY


@python_2_unicode_compatible
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    max_number_workers = models.IntegerField(default=100)
    city = models.ForeignKey(City, related_name='cities', on_delete=models.SET_NULL, null=True)
    province = models.ForeignKey(Province, related_name='provinces', on_delete=models.SET_NULL, null=True)
    country = models.CharField(
        max_length=50,
        choices=COUNTRY_ENUM_CHOICE,
        default=DEFAULT_COUNTRY
    )

    class Meta(object):
        verbose_name = _("Hospital")
        verbose_name_plural = _("Hospitals")
        ordering = ["name"]

    def __str__(self):
        return self.name
