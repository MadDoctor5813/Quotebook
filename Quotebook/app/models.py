"""
Definition of models.
"""

from django.contrib import admin
from django.db import models

class Quote(models.Model):

    quote = models.CharField(max_length=128)
    attribution = models.CharField(max_length=64)

    rating = models.FloatField(default=0)
    num_ratings = models.IntegerField(default=0);

    def __str__(self):
        return 'Quote ' + str(self.pk) + ' by ' + self.attribution

class SubmittedQuote(models.Model):

    quote = models.CharField(max_length=128)
    attribution = models.CharField(max_length=64)
    submitter_email = models.EmailField(blank=True)
    date_submitted = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Quote submitted by ' + self.submitter_email
