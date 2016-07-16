'''
Created on Jul 15, 2016

@author: Brian
'''
from django.conf.urls import include, url
from django.contrib import admin

from home.views import Index


urlpatterns = [
    url(r'', Index.as_view()),
]
