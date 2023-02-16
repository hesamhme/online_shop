from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'


class AboutUsPage(TemplateView):
    template_name = 'pages/about.html'
