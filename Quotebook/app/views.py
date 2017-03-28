"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
from django.template import RequestContext
from django.core.exceptions import SuspiciousOperation
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from app.models import Quote
from app.models import SubmittedQuote
from datetime import datetime
import random

def view_quote(request, page_id=None):
    if page_id == None:
        #no specific quote requested, display a random one
        quote = random.choice(Quote.objects.all())
    else:
        #display a quote with the requested id
        quote = Quote.objects.get(pk=page_id)
    return render(request, "app/view_quote.html", {'quote': quote})

def view_all_quotes(request):
    search = request.GET.get('search')
    if search:
        quote_set = Quote.objects.none()
        if request.GET.get('searchAuthor'):
            quote_set = quote_set | Quote.objects.filter(attribution__icontains=search)
        if request.GET.get('searchText'):
            quote_set = quote_set | Quote.objects.filter(quote__icontains=search)
    else:
        quote_set = Quote.objects.all().order_by("-pk")

    sort = request.GET.get('sort')
    if sort == 'ratingAscend':
        quote_set = quote_set.order_by('rating', '-pk')
    elif sort == 'ratingDescend':
        quote_set = quote_set.order_by('-rating', '-pk')
    elif sort == 'numRatingsAscend':
        quote_set = quote_set.order_by('num_ratings', '-pk')
    elif sort == 'numRatingsDescend':
        quote_set = quote_set.order_by('-num_ratings', '-pk')

    paginator = Paginator(quote_set, 5)
    try:
        page_num = request.GET['page']
        quotes = paginator.page(page_num)
    except MultiValueDictKeyError:
        #if there's no page param, return the first page
        quotes = paginator.page(1)

    return render(request, "app/all_quotes.html", {'quotes' : quotes})

def submit_quote(request):
    if request.method == 'GET':
        #if it's a get, just render the submission form
        return render(request, 'app/submit_quote.html')
    elif request.method == 'POST':
        #this is a form submission
        submitted = SubmittedQuote()
        submitted.quote = request.POST['quote']
        submitted.attribution = request.POST['author']
        submitted.submitter_email = request.POST['submitterEmail']
        submitted.save()
        return render(request, 'app/submit_success.html')

def rate_quote(request):
    new_rating = float(request.POST['rating'])
    #check if the rating is out of range
    if new_rating < 0 or new_rating > 5:
        raise SuspiciousOperation
    quote_id = int(request.POST['id'])
    quote = Quote.objects.get(pk=quote_id)
    #calculate a new average rating
    rating_sum = quote.rating * quote.num_ratings
    rating_sum += new_rating
    quote.num_ratings += 1
    quote.rating = rating_sum / quote.num_ratings
    quote.save()
    return JsonResponse({'rating' : quote.rating, 'num_ratings': quote.num_ratings})