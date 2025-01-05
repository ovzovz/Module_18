from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

def start(request):
    return render(request, 'platform.html')

def get_catalog(request):
    tours = {'tour1': 'Северная Венеция',
             'tour2': 'Золотое кольцо',
             'tour3': 'Янтарный берег'}
    return render(request, 'catalog.html',
                  context= tours)

class ClassCart(TemplateView):
    template_name = 'cart.html'
