'''
Created on Jul 15, 2016

@author: Brian
'''
from django.forms import ModelForm
from habitat.models import PokemonSighting

class PokemonSightingForm(ModelForm):
    class Meta:
        model = PokemonSighting
        fields = ['name','location']
        
    