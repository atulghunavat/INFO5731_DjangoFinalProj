import base64
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
import io
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from mysite.settings import *
from .models import *
import pickle
from project.models import *



def index(request):
    return HttpResponse("Hello, world. You're at the Paper index.")

def paperlist(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        #This saves objects to the papers module
        p = Papers()
        p.Paper_Title = uploaded_file.name
        file = io.BytesIO(uploaded_file.read())
        p.Paper_Content = convertContentToText(file).encode()
        p.Project_ID = Project.objects.all()[0]
        p.save()
        return HttpResponseRedirect(request.path_info)
    return render(request, 'paperlist.html', {'paper_list':Papers.objects.all()})

def convertContentToText(file):
    parser = PDFParser(file)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    laparams.char_margin = 1.0
    laparams.word_margin = 1.0
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    extracted_text = ''

    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                extracted_text += lt_obj.get_text()
    return extracted_text

def papercontent(request):
    paper_id = request.GET.get("Paper_ID")
    p = Papers.objects.get(Paper_ID=paper_id)
    content = p.Paper_Content.decode()
    return render(request, 'papercontent.html', {'paper_content':content})

# def contentdemo(request):
#     return render(request, 'contentdemo.html')

def paperannotation(request):
    return render(request, 'annotation.html')


# def papers(request):
#     return render(request, 'papers/')
#     paper1 = papers.objects.get(pk=paper_id)
#     return HttpResponse("You're looking at papers %s." % paper1.paper_title)