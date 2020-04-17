# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def paperlist(request):
    return render(request, 'paperlist.html')

def papercontent(request):
    return render(request, 'papercontent.html')

def paperannotation(request):
    return render(request, 'annotation.html')


# def paper(request):
#     return render(request, 'polls/')
#     # paper1 = paper.objects.get(pk=paper_id)
#     # return HttpResponse("You're looking at paper %s." % paper1.paper_title)