from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the Project index.")

def projectlist(request):
    if request.method == 'POST':
        if request.POST.get('projectname'):
            #This saves objects to the papers module
            p = Project()
            p.Project_Title = request.POST.get('projectname')
            p.Project_Description = request.POST.get('description')
            p.save()
        return HttpResponseRedirect(request.path_info)
    return render(request, 'projectlist.html', {'project_list':Project.objects.all()})