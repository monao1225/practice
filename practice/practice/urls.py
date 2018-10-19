"""
Definition of urls for practice.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf.urls import include
import django.contrib.auth.views

import HelloDjango.views

# Uncomment the next lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
   url(r'^$', HelloDjango.views.index, name='index'),
   url(r'^home$', HelloDjango.views.index, name='home'),
   url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^about$',HelloDjango.views.about, name='about')
]
