from django.db import models


class Entry(models.Model):
    '''Model for entry
    '''

    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=254)

    class Meta:
        ordering = ('name',)
