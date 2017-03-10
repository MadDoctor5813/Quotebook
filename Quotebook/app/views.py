"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.core.paginator import Paginator
from app.models import Quote
from datetime import datetime
import random

def view_quote(request):
    random_quote = random.choice(Quote.objects.all())
    return render(request, "app/quote.html", {'quote': random_quote.quote, 'attribution': random_quote.attribution})

def view_all_quotes(request):
    all_quotes = Quote.objects.all()
    paginator = Paginator(all_quotes, 5)
    return render(request, "app/all_quotes.html", {'quotes' : paginator.page(request.GET['page']), 'page_obj' : paginator.page(request.GET['page'])})