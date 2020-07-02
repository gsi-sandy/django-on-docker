from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name
