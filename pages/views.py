from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

# class HomePageView(TemplateView):
#     template_name = 'pages/home.html'
#
#
# class AboutPageView(TemplateView):
#     template_name = 'pages/about.html'


def home_page(request):
    return render(request, 'pages/home.html')


def about_page(request):
    return render(request, 'pages/about.html')
