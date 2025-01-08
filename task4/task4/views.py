from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

def start(request):
    title = 'Главная страница'
    context = {'title':title}
    return render(request, 'platform.html', context)

def get_catalog(request):
    title = 'Каталог туров'
   # tours = {'tours': ['Северная Венеция','Золотое кольцо', 'Янтарный берег']}
    context = {'title':title, 'tours': ['Северная Венеция','Золотое кольцо', 'Янтарный берег']}
    return render(request, 'catalog.html', context)

class ClassCart(TemplateView):
    template_name = 'cart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Корзина"
        return context