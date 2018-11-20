from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def homepage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request, 'index.html'))
    
def eggs(request):
    return HttpResponse('<h1>Eggs</h1>')


