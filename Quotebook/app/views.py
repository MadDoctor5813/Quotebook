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

def view_quote(request, page_id=None):
    if page_id == None:
        #no specific quote requested, display a random one
        quote = random.choice(Quote.objects.all())
    else:
        #display a quote with the requested id
        quote = Quote.objects.get(pk=page_id)
    return render(request, "app/quote.html", {'quote': quote})

def view_all_quotes(request):
    try:
        search = request.GET['search']
        searchType = request.GET['searchType']
        if searchType == 'text':
            quote_set = Quote.objects.filter(quote__icontains=search)
        elif searchType == 'author':
            quote_set = Quote.objects.filter(attribution__icontains=search)
    except MultiValueDictKeyError:
        quote_set = Quote.objects.all()
    paginator = Paginator(quote_set, 5)
    try:
        page_num = request.GET['page']
        quotes = paginator.page(page_num)
    except MultiValueDictKeyError:
        #if there's no page param, return the first page
        quotes = paginator.page(1)

    return render(request, "app/all_quotes.html", {'quotes' : quotes})