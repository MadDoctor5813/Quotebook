"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.utils.datastructures import MultiValueDictKeyError
from app.models import Quote
from datetime import datetime
import random

def view_quote(request):
    random_quote = random.choice(Quote.objects.all())
    return render(request, "app/quote.html", {'quote': random_quote.quote, 'attribution': random_quote.attribution})

def view_all_quotes(request):
    all_quotes = Quote.objects.all()
    try:
        page_num = request.GET['page']
        quotes = paginator.page(page_num)
    except MultiValueDictKeyError:
        #if there's no page param, return the first page
        quotes = paginator.page(1)

    return render(request, "app/all_quotes.html", {'quotes' : quotes})