from django.shortcuts import render
from habitat.forms import PokemonSightingForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

class ReportPokemonSighting(FormView):
    template_name='habitat/pokemonsighting.html'
    form_class=PokemonSightingForm
    success_url='reported'
    