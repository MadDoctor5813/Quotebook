"""
Definition of models.
"""

from django.contrib import admin
from django.db import models

class Quote(models.Model):

    quote = models.CharField(max_length=128)
    attribution = models.CharField(max_length=64)

    def __str__(self):
        return 'Quote ' + str(self.pk) + ' by ' + self.attribution

admin.site.register(Quote)