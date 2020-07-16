from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from six import python_2_unicode_compatible
from ..models.province import Province


@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, related_name='province', on_delete=models.CASCADE)

    class Meta(object):
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
            return self.name
