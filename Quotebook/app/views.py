"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from app.models import Quote
from datetime import datetime
import random

def view_quote(request):
    random_quote = random.choice(Quote.objects.all())
    return render(request, "app/quote.html", {'quote': random_quote.quote, 'attribution': random_quote.attribution})