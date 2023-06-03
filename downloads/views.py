from django.shortcuts import render
from forms.forms import *
from forms.models import *
from django.template.loader import get_template
import pdfkit
from django.http import HttpResponse
from django.conf import settings
from home.decorators import allowed_users
import os
import base64
from datetime import date, datetime



# Create your views here.
def download(request):
    current_SY1 = datetime.now().year
    current_SY2 = current_SY1 - 1
    
    last_SY1 = current_SY2
    last_SY2 = last_SY1 - 1
    
    last_last_SY1 = last_SY2
    last_last_SY2 = last_last_SY1 - 1
    
    context = {
        'current_SY1' : current_SY1,
        'current_SY2' : current_SY2,
        'last_SY1' : last_SY1,
        'last_SY2' : last_SY2,
        'last_last_SY1' : last_last_SY1,
        'last_last_SY2' : last_last_SY2,
    }
    
    return render(request, ('downloads/IPCR_Download.html'), context)

def image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def firstmidsem_ViewIPCR(request):
    current_year = datetime.now().year
    actual_year = current_year - 1
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def firstfinalsem_ViewIPCR(request):
    current_year = datetime.now().year
    actual_year = current_year - 1
    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25

    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(current_year, firstsem_endmonth, firstsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def secondmidsem_ViewIPCR(request):
    current_year = datetime.now().year
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_day = 5
    
    secondmidsem_date = datetime(current_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(current_year, secondfinalsem_month, secondsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def secondfinalsem_ViewIPCR(request):
    current_year = datetime.now().year
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    secondfinalsem_date = datetime(current_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(current_year, secondsem_endmonth, secondsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Rating.DoesNotExist:
        data3 = None


    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def firstmidsem_download_pdf(request):
    current_year = datetime.now().year
    actual_year = current_year - 1
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target003.png',
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target004.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    base64_string4 = image_to_base64(image_paths[3])
    
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    'base64_string4': base64_string4,}
                                   , request)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    options = {
        'allow': [os.path.join(settings.STATICFILES_DIRS[0], 'IPCR')],
        'quiet': '',
        'enable-local-file-access': True,
        'encoding': 'UTF-8',
        'no-outline': None,
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'letter',
        'dpi': '300',
        'print-media-type': None,
        'no-collate': None,
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPCRForm_FirstSemFinalTerm.pdf"'
    return response

def firstfinalsem_download_pdf(request):
    current_year = datetime.now().year
    actual_year = current_year - 1
    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25

    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(current_year, firstsem_endmonth, firstsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target003.png',
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target004.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    base64_string4 = image_to_base64(image_paths[3])
    
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    'base64_string4': base64_string4,}
                                   , request)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    options = {
        'allow': [os.path.join(settings.STATICFILES_DIRS[0], 'IPCR')],
        'quiet': '',
        'enable-local-file-access': True,
        'encoding': 'UTF-8',
        'no-outline': None,
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'letter',
        'dpi': '300',
        'print-media-type': None,
        'no-collate': None,
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPCRForm_FirstSemFinalTerm.pdf"'
    return response

def secondmidsem_download_pdf(request):
    current_year = datetime.now().year
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_day = 5
    
    secondmidsem_date = datetime(current_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(current_year, secondfinalsem_month, secondsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target003.png',
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target004.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    base64_string4 = image_to_base64(image_paths[3])
    
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    'base64_string4': base64_string4,}
                                   , request)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    options = {
        'allow': [os.path.join(settings.STATICFILES_DIRS[0], 'IPCR')],
        'quiet': '',
        'enable-local-file-access': True,
        'encoding': 'UTF-8',
        'no-outline': None,
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'letter',
        'dpi': '300',
        'print-media-type': None,
        'no-collate': None,
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPCRForm_SecondSemMidTerm.pdf"'
    return response

def secondfinalsem_download_pdf(request):
    current_year = datetime.now().year
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    secondfinalsem_date = datetime(current_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(current_year, secondsem_endmonth, secondsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target003.png',
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target004.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    base64_string4 = image_to_base64(image_paths[3])
    
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    'base64_string4': base64_string4,}
                                   , request)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    options = {
        'allow': [os.path.join(settings.STATICFILES_DIRS[0], 'IPCR')],
        'quiet': '',
        'enable-local-file-access': True,
        'encoding': 'UTF-8',
        'no-outline': None,
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'letter',
        'dpi': '300',
        'print-media-type': None,
        'no-collate': None,
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPCRForm_SecondSemFinalTerm.pdf"'
    return response

def last_firstmidsem_ViewIPCR(request):
    current_year = datetime.now().year
    actual_year = current_year - 2
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def last_firstfinalsem_ViewIPCR(request):
    current_year = datetime.now().year
    actual_year = current_year - 2
    actual_actual_year = current_year - 1
    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25

    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(actual_actual_year, firstsem_endmonth, firstsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def last_secondmidsem_ViewIPCR(request):
    current_year = datetime.now().year
    actual_year = current_year - 1
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_day = 5
    
    secondmidsem_date = datetime(actual_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def last_secondfinalsem_ViewIPCR(request):
    current_year = datetime.now().year
    actual_year = current_year - 1
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(actual_year, secondsem_endmonth, secondsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Rating.DoesNotExist:
        data3 = None


    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def last_firstmidsem_download_pdf(request):
    current_year = datetime.now().year
    actual_year = current_year - 2
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Rating.DoesNotExist:
        data3 = None


    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target003.png',
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target004.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    base64_string4 = image_to_base64(image_paths[3])
    
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    'base64_string4': base64_string4,}
                                   , request)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    options = {
        'allow': [os.path.join(settings.STATICFILES_DIRS[0], 'IPCR')],
        'quiet': '',
        'enable-local-file-access': True,
        'encoding': 'UTF-8',
        'no-outline': None,
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'letter',
        'dpi': '300',
        'print-media-type': None,
        'no-collate': None,
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPCRForm_FirstSemFinalTerm.pdf"'
    return response

def last_firstfinalsem_download_pdf(request):
    current_year = datetime.now().year
    actual_year = current_year - 2
    actual_actual_year = current_year - 1
    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25

    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(actual_actual_year, firstsem_endmonth, firstsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target003.png',
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target004.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    base64_string4 = image_to_base64(image_paths[3])
    
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    'base64_string4': base64_string4,}
                                   , request)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    options = {
        'allow': [os.path.join(settings.STATICFILES_DIRS[0], 'IPCR')],
        'quiet': '',
        'enable-local-file-access': True,
        'encoding': 'UTF-8',
        'no-outline': None,
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'letter',
        'dpi': '300',
        'print-media-type': None,
        'no-collate': None,
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPCRForm_FirstSemFinalTerm.pdf"'
    return response

def last_secondmidsem_download_pdf(request):
    current_year = datetime.now().year
    actual_year = current_year - 1
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_day = 5
    
    secondmidsem_date = datetime(actual_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target003.png',
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target004.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    base64_string4 = image_to_base64(image_paths[3])
    
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    'base64_string4': base64_string4,}
                                   , request)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    options = {
        'allow': [os.path.join(settings.STATICFILES_DIRS[0], 'IPCR')],
        'quiet': '',
        'enable-local-file-access': True,
        'encoding': 'UTF-8',
        'no-outline': None,
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'letter',
        'dpi': '300',
        'print-media-type': None,
        'no-collate': None,
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPCRForm_SecondSemMidTerm.pdf"'
    return response

def last_secondfinalsem_download_pdf(request):
    current_year = datetime.now().year
    actual_year = current_year - 1
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(actual_year, secondsem_endmonth, secondsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Rating.DoesNotExist:
        data3 = None


    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target003.png',
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target004.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    base64_string4 = image_to_base64(image_paths[3])
    
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    'base64_string4': base64_string4,}
                                   , request)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    options = {
        'allow': [os.path.join(settings.STATICFILES_DIRS[0], 'IPCR')],
        'quiet': '',
        'enable-local-file-access': True,
        'encoding': 'UTF-8',
        'no-outline': None,
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'letter',
        'dpi': '300',
        'print-media-type': None,
        'no-collate': None,
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPCRForm_SecondSemFinalTerm.pdf"'
    return response

def last_last_firstmidsem_ViewIPCR(request):
    current_year = datetime.now().year
    actual_year = current_year - 3
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def last_last_firstfinalsem_ViewIPCR(request):
    current_year = datetime.now().year
    actual_year = current_year - 3
    actual_actual_year = current_year - 2
    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25

    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(actual_actual_year, firstsem_endmonth, firstsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def last_last_secondmidsem_ViewIPCR(request):
    current_year = datetime.now().year
    actual_year = current_year - 2
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_day = 5
    
    secondmidsem_date = datetime(actual_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def last_last_secondfinalsem_ViewIPCR(request):
    current_year = datetime.now().year
    actual_year = current_year - 2
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(actual_year, secondsem_endmonth, secondsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Rating.DoesNotExist:
        data3 = None


    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def last_last_firstmidsem_download_pdf(request):
    current_year = datetime.now().year
    actual_year = current_year - 3
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPCR_Rating.DoesNotExist:
        data3 = None


    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target003.png',
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target004.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    base64_string4 = image_to_base64(image_paths[3])
    
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    'base64_string4': base64_string4,}
                                   , request)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    options = {
        'allow': [os.path.join(settings.STATICFILES_DIRS[0], 'IPCR')],
        'quiet': '',
        'enable-local-file-access': True,
        'encoding': 'UTF-8',
        'no-outline': None,
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'letter',
        'dpi': '300',
        'print-media-type': None,
        'no-collate': None,
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPCRForm_FirstSemFinalTerm.pdf"'
    return response

def last_last_firstfinalsem_download_pdf(request):
    current_year = datetime.now().year
    actual_year = current_year - 3
    actual_actual_year = current_year - 2
    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25

    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(actual_actual_year, firstsem_endmonth, firstsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target003.png',
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target004.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    base64_string4 = image_to_base64(image_paths[3])
    
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    'base64_string4': base64_string4,}
                                   , request)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    options = {
        'allow': [os.path.join(settings.STATICFILES_DIRS[0], 'IPCR')],
        'quiet': '',
        'enable-local-file-access': True,
        'encoding': 'UTF-8',
        'no-outline': None,
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'letter',
        'dpi': '300',
        'print-media-type': None,
        'no-collate': None,
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPCRForm_FirstSemFinalTerm.pdf"'
    return response

def last_last_secondmidsem_download_pdf(request):
    current_year = datetime.now().year
    actual_year = current_year - 2
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_day = 5
    
    secondmidsem_date = datetime(actual_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPCR_Rating.DoesNotExist:
        data3 = None

    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target003.png',
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target004.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    base64_string4 = image_to_base64(image_paths[3])
    
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    'base64_string4': base64_string4,}
                                   , request)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    options = {
        'allow': [os.path.join(settings.STATICFILES_DIRS[0], 'IPCR')],
        'quiet': '',
        'enable-local-file-access': True,
        'encoding': 'UTF-8',
        'no-outline': None,
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'letter',
        'dpi': '300',
        'print-media-type': None,
        'no-collate': None,
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPCRForm_SecondSemMidTerm.pdf"'
    return response

def last_last_secondfinalsem_download_pdf(request):
    current_year = datetime.now().year
    actual_year = current_year - 2
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(actual_year, secondsem_endmonth, secondsem_day).date()
    
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPCR_Rating.DoesNotExist:
        data3 = None


    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target003.png',
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target004.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    base64_string4 = image_to_base64(image_paths[3])
    
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    'base64_string4': base64_string4,}
                                   , request)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    options = {
        'allow': [os.path.join(settings.STATICFILES_DIRS[0], 'IPCR')],
        'quiet': '',
        'enable-local-file-access': True,
        'encoding': 'UTF-8',
        'no-outline': None,
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'letter',
        'dpi': '300',
        'print-media-type': None,
        'no-collate': None,
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPCRForm_SecondSemFinalTerm.pdf"'
    return response
