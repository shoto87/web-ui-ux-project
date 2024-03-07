from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('carouseltest7.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def carouseltest7(request):
    return render(request, 'carouseltest7.html')

def community(request):
    return render(request, 'community.html')

def support(request):
    return render(request, 'support.html')
