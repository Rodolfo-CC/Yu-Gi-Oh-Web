from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class DetailsPageView(TemplateView):
    template_name = 'details.html'
