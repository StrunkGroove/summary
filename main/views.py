from django.shortcuts import render
from django.http import FileResponse
from django.http import HttpResponse
from django.conf import settings
import os


def index(request):
    return render(request, 'main/index.html')

def summary(request):
    return render(request, 'main/summary.html')

def download_summary(request):
    pdf_file_path = os.path.join(settings.MEDIA_ROOT, 'main/pdfs', 'Резюме.pdf')
    response = FileResponse(open(pdf_file_path, 'rb'), as_attachment=True)
    return response

def my_project(request):
    return render(request, 'main/my_project.html')

def download_my_project(request):
    pdf_file_path = os.path.join(settings.MEDIA_ROOT, 'main/pdfs', 'Портфолио.pdf')
    response = FileResponse(open(pdf_file_path, 'rb'), as_attachment=True)
    return response