from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from six import python_2_unicode_compatible


@python_2_unicode_compatible
class Province(models.Model):
    name = models.CharField(max_length=100)

    class Meta(object):
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')

    def __str__(self):
            return self.name
