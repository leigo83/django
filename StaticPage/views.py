from django.shortcuts import render
from django.views.generic import TemplateView

class HelloDjango(TemplateView):
    template_name = "test.html"

# Create your views here.
