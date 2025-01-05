from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

def start(request):
    return HttpResponse("Добро пожаловать!")

def func_demo(request):
    return render(request, 'func_template.html')

class ClassDemo(TemplateView):
    template_name = 'class_template.html'
