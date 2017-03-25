"""
Definition of urls for Quotebook.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.view_quote),
	url(r'^(?P<page_id>\d+)/$', app.views.view_quote), 

    url(r'^all_quotes/$', app.views.view_all_quotes),

    url(r'^submit_quote/$', app.views.submit_quote),

    url(r'^api/rate_quote/$', app.views.rate_quote),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
