# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import *
import uuid

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def paperlist(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        #This saves objects to the paper module
        all_papers = Paper.objects.all()
        p = Paper()
        if len(all_papers) > 0:
            paper_with_max_id = all_papers.order_by("-Paper_ID")[0]
            p.Paper_ID = int(paper_with_max_id.Paper_ID + 1)
        else:
            p.Paper_ID = 1
        p.Paper_Title = uploaded_file.name
        p.Paper_Content = uploaded_file
        p.Project_ID = Project.objects.all()[0]
        p.save()
        return HttpResponseRedirect(request.path_info)
    return render(request, 'paperlist.html', {'paper_list':Paper.objects.all()})


def papercontent(request):
    return render(request, 'papercontent.html')

def paperannotation(request):
    return render(request, 'annotation.html')


# def paper(request):
#     return render(request, 'polls/')
#     # paper1 = paper.objects.get(pk=paper_id)
#     # return HttpResponse("You're looking at paper %s." % paper1.paper_title)