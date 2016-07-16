'''
Created on Jul 15, 2016

@author: Brian
'''
from django.conf.urls import include, url
from django.contrib import admin
from .views import ReportPokemonSighting

urlpatterns = [
    url(r'^add-pokemon-sighting/', ReportPokemonSighting.as_view()),
]
