from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name="gobblehome/index.html"