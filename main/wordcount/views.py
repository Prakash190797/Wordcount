from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")
    
def eggs(request):
    return HttpResponse('<h1>Eggs</h1>')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist)})
    



