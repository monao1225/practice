"""
Definition of urls for practice.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import HelloDjango.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
   url(r'^$', HelloDjango.views.index, name='index'),
   url(r'^home$', HelloDjango.views.index, name='home'),
]
