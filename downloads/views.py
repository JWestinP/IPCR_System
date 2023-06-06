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
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def download(request):
    current_user = request.user
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
        'current_user' : current_user,
    }
    
    return render(request, ('downloads/IPCR_Download.html'), context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def download_ipmt(request):
    current_user = request.user

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
        'current_user' : current_user,

    }
    
    return render(request, ('downloads/IPMT_Download.html'), context)

def image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

#IPCR Forms
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def firstmidsem_ViewIPCR(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 8 and current_month <= 10:
        actual_year = current_year
    else:
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def firstfinalsem_ViewIPCR(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 10 and current_month <= 12:
        actual_year = current_year
    else:
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def secondfinalsem_ViewIPCR(request):
    current_year = datetime.now().year
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 10
    
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def firstmidsem_download_pdf(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 8 and current_month <= 10:
        actual_year = current_year
    else:
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def firstfinalsem_download_pdf(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 10 and current_month <= 12:
        actual_year = current_year
    else:
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def secondfinalsem_download_pdf(request):
    current_year = datetime.now().year
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 10
    
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_firstmidsem_ViewIPCR(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 8 and current_month <= 10:
        actual_year = current_year - 1
    else:
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_firstfinalsem_ViewIPCR(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 10 and current_month <= 12:
        actual_year = current_year - 1
        actual_actual_year = current_year
    else:
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_firstmidsem_download_pdf(request):
    current_year = datetime.now().year
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 8 and current_month <= 10:
        actual_year = current_year - 1
    else:
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_firstfinalsem_download_pdf(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 10 and current_month <= 12:
        actual_year = current_year - 1
        actual_actual_year = current_year
    else:
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_last_firstmidsem_ViewIPCR(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 8 and current_month <= 10:
        actual_year = current_year - 2
    else:
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_last_firstfinalsem_ViewIPCR(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 10 and current_month <= 12:
        actual_year = current_year - 2
        actual_actual_year = current_year - 1
    else:
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_last_firstmidsem_download_pdf(request):
    current_year = datetime.now().year
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 8 and current_month <= 10:
        actual_year = current_year - 2
    else:
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_last_firstfinalsem_download_pdf(request):
    current_year = datetime.now().year
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 10 and current_month <= 12:
        actual_year = current_year - 2
        actual_actual_year = current_year - 1
    else:
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
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

#IPMT Forms
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def firstmidsem_ViewIPMT(request):
    current_year = datetime.now().year
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 8 and current_month <= 10:
        actual_year = current_year
    else:
        actual_year = current_year - 1
    
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    try: 
        data8 = IPMT_Form_model_submitted_8.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_8.DoesNotExist:
        data8 = None
        
    try: 
        data9 = IPMT_Form_model_submitted_9.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_9.DoesNotExist:
        data9 = None
        
    try: 
        data10 = IPMT_Form_model_submitted_10.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_10.DoesNotExist:
        data10 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None    
        
    data1 = None
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    data7 = None
    data11 = None
    data12 = None
    
    context = {
        'data1': data1,
        'data2' : data2,
        'data3' : data3,
        'data4' : data4,
        'data5' : data5,
        'data6' : data6,
        'data7' : data7,
        'data8' : data8,
        'data9' : data9,
        'data10' : data10,
        'data11' : data11,
        'data12' : data12,
        'data' : data
    }
    return render(request, 'downloads/IPMTForm.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def firstfinalsem_ViewIPMT(request):
    current_year = datetime.now().year
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 10 and current_month <= 12:
        actual_year = current_year
    else:
        actual_year = current_year - 1
    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25

    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(current_year, firstsem_endmonth, firstsem_day).date()
    
    try: 
        data10 = IPMT_Form_model_submitted_10.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_10.DoesNotExist:
        data10 = None

    try: 
        data11 = IPMT_Form_model_submitted_11.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_11.DoesNotExist:
        data11 = None
    
    try: 
        data12 = IPMT_Form_model_submitted_12.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_12.DoesNotExist:
        data12 = None
        
    try: 
        data1 = IPMT_Form_model_submitted_1.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_1.DoesNotExist:
        data1 = None

    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Remarks.DoesNotExist:
        data = None
        
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    data7 = None
    data8 = None
    data9 = None
    
    context = {
        'data1': data1,
        'data2' : data2,
        'data3' : data3,
        'data4' : data4,
        'data5' : data5,
        'data6' : data6,
        'data7' : data7,
        'data8' : data8,
        'data9' : data9,
        'data10' : data10,
        'data11' : data11,
        'data12' : data12,
        'data' : data
    }

    return render(request, 'downloads/IPMTForm.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def secondmidsem_ViewIPMT(request):
    current_year = datetime.now().year
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_day = 5
    
    secondmidsem_date = datetime(current_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(current_year, secondfinalsem_month, secondsem_day).date()
    
    try: 
        data2 = IPMT_Form_model_submitted_2.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_2.DoesNotExist:
        data2 = None

    try: 
        data3 = IPMT_Form_model_submitted_3.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_3.DoesNotExist:
        data3 = None
    
    try: 
        data4 = IPMT_Form_model_submitted_4.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_4.DoesNotExist:
        data4 = None

    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None
        
    data1 = None        
    data5 = None
    data6 = None
    data7 = None
    data8 = None
    data9 = None
    data10 = None
    data11 = None
    data12 = None
    
    context = {
        'data1': data1,
        'data2' : data2,
        'data3' : data3,
        'data4' : data4,
        'data5' : data5,
        'data6' : data6,
        'data7' : data7,
        'data8' : data8,
        'data9' : data9,
        'data10' : data10,
        'data11' : data11,
        'data12' : data12,
        'data' : data
    }

    return render(request, 'downloads/IPCRForm.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def secondfinalsem_ViewIPMT(request):
    current_year = datetime.now().year
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 10
    
    secondfinalsem_date = datetime(current_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(current_year, secondsem_endmonth, secondsem_day).date()
    
    try: 
        data4 = IPMT_Form_model_submitted_4.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_4.DoesNotExist:
        data4 = None

    try: 
        data5 = IPMT_Form_model_submitted_5.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_5.DoesNotExist:
        data5 = None

    try: 
        data6 = IPMT_Form_model_submitted_6.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_6.DoesNotExist:
        data6 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Remarks.DoesNotExist:
        data = None
    
    
    data1 = None
    data2 = None
    data3 = None
    data7 = None
    data8 = None
    data9 = None
    data10 = None
    data11 = None
    data12 = None
    
    context = {
        'data1': data1,
        'data2' : data2,
        'data3' : data3,
        'data4' : data4,
        'data5' : data5,
        'data6' : data6,
        'data7' : data7,
        'data8' : data8,
        'data9' : data9,
        'data10' : data10,
        'data11' : data11,
        'data12' : data12,
        'data' : data
    }

    return render(request, 'downloads/IPMTForm.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def firstmidsem_DownloadIPMT(request):
    current_year = datetime.now().year
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 8 and current_month <= 10:
        actual_year = current_year
    else:
        actual_year = current_year - 1
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    try: 
        data8 = IPMT_Form_model_submitted_8.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_8.DoesNotExist:
        data8 = None
        
    try: 
        data9 = IPMT_Form_model_submitted_9.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_9.DoesNotExist:
        data9 = None
        
    try: 
        data10 = IPMT_Form_model_submitted_10.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_10.DoesNotExist:
        data10 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None    
        
    data1 = None
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    data7 = None
    data11 = None
    data12 = None
    
    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target003.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    
    
    template = get_template('downloads/IPMTForm_Download.html')
    html_content = template.render({'data1': data1,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'data4' : data4,
                                    'data5' : data5,
                                    'data6' : data6,
                                    'data7' : data7,
                                    'data8' : data8,
                                    'data9' : data9,
                                    'data10' : data10,
                                    'data11' : data11,
                                    'data12' : data12,
                                    'data' : data,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    }
                                    ,request)

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
        'orientation': 'Landscape'
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPMTForm_FirstSemMidTerm.pdf"'
    return response

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def firstfinalsem_DownloadIPMT(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 10 and current_month <= 12:
        actual_year = current_year
    else:
        actual_year = current_year - 1
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    try: 
        data8 = IPMT_Form_model_submitted_8.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_8.DoesNotExist:
        data8 = None
        
    try: 
        data9 = IPMT_Form_model_submitted_9.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_9.DoesNotExist:
        data9 = None
        
    try: 
        data10 = IPMT_Form_model_submitted_10.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_10.DoesNotExist:
        data10 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None    
        
    data1 = None
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    data7 = None
    data11 = None
    data12 = None
    
    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target003.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    
    
    template = get_template('downloads/IPMTForm_Download.html')
    html_content = template.render({'data1': data1,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'data4' : data4,
                                    'data5' : data5,
                                    'data6' : data6,
                                    'data7' : data7,
                                    'data8' : data8,
                                    'data9' : data9,
                                    'data10' : data10,
                                    'data11' : data11,
                                    'data12' : data12,
                                    'data' : data,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    }
                                    ,request)

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
        'orientation': 'Landscape'
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPMTForm_FirstSemFinalTerm.pdf"'
    return response

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def secondmidsem_DownloadIPMT(request):
    current_year = datetime.now().year
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_day = 5
    
    secondmidsem_date = datetime(current_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(current_year, secondfinalsem_month, secondsem_day).date()
    
    try: 
        data2 = IPMT_Form_model_submitted_2.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_2.DoesNotExist:
        data2 = None

    try: 
        data3 = IPMT_Form_model_submitted_3.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_3.DoesNotExist:
        data3 = None
    
    try: 
        data4 = IPMT_Form_model_submitted_4.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_4.DoesNotExist:
        data4 = None

    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None
        
    data1 = None        
    data5 = None
    data6 = None
    data7 = None
    data8 = None
    data9 = None
    data10 = None
    data11 = None
    data12 = None
    
    
    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target003.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    
    
    template = get_template('downloads/IPMTForm_Download.html')
    html_content = template.render({'data1': data1,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'data4' : data4,
                                    'data5' : data5,
                                    'data6' : data6,
                                    'data7' : data7,
                                    'data8' : data8,
                                    'data9' : data9,
                                    'data10' : data10,
                                    'data11' : data11,
                                    'data12' : data12,
                                    'data' : data,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    }
                                    ,request)

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
        'orientation': 'Landscape'
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPMTForm_SecondSemMidTerm.pdf"'
    return response

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def secondfinalsem_DownloadIPMT(request):
    current_year = datetime.now().year
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    secondfinalsem_date = datetime(current_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(current_year, secondsem_endmonth, secondsem_day).date()
    
    try: 
        data4 = IPMT_Form_model_submitted_4.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_4.DoesNotExist:
        data4 = None

    try: 
        data5 = IPMT_Form_model_submitted_5.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_5.DoesNotExist:
        data5 = None

    try: 
        data6 = IPMT_Form_model_submitted_6.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_6.DoesNotExist:
        data6 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Remarks.DoesNotExist:
        data = None
    
    
    data1 = None
    data2 = None
    data3 = None
    data7 = None
    data8 = None
    data9 = None
    data10 = None
    data11 = None
    data12 = None
    
    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target003.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    
    
    template = get_template('downloads/IPMTForm_Download.html')
    html_content = template.render({'data1': data1,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'data4' : data4,
                                    'data5' : data5,
                                    'data6' : data6,
                                    'data7' : data7,
                                    'data8' : data8,
                                    'data9' : data9,
                                    'data10' : data10,
                                    'data11' : data11,
                                    'data12' : data12,
                                    'data' : data,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    }
                                    ,request)

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
        'orientation': 'Landscape'
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPMTForm_SecondSemFinalTerm.pdf"'
    return response

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_firstmidsem_ViewIPMT(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 8 and current_month <= 10:
        actual_year = current_year - 1
    else:
        actual_year = current_year - 2
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    try: 
        data8 = IPMT_Form_model_submitted_8.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_8.DoesNotExist:
        data8 = None
        
    try: 
        data9 = IPMT_Form_model_submitted_9.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_9.DoesNotExist:
        data9 = None
        
    try: 
        data10 = IPMT_Form_model_submitted_10.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_10.DoesNotExist:
        data10 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None    
        
    data1 = None
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    data7 = None
    data11 = None
    data12 = None
    
    context = {
        'data1': data1,
        'data2' : data2,
        'data3' : data3,
        'data4' : data4,
        'data5' : data5,
        'data6' : data6,
        'data7' : data7,
        'data8' : data8,
        'data9' : data9,
        'data10' : data10,
        'data11' : data11,
        'data12' : data12,
        'data' : data
    }
    return render(request, 'downloads/IPMTForm.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_firstfinalsem_ViewIPMT(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 10 and current_month <= 12:
        actual_year = current_year - 1
        actual_actual_year = current_year
    else:
        actual_year = current_year - 2
        actual_actual_year = current_year - 1

    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25

    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(actual_actual_year, firstsem_endmonth, firstsem_day).date()
    
    
    try: 
        data10 = IPMT_Form_model_submitted_10.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_10.DoesNotExist:
        data10 = None

    try: 
        data11 = IPMT_Form_model_submitted_11.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_11.DoesNotExist:
        data11 = None
    
    try: 
        data12 = IPMT_Form_model_submitted_12.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_12.DoesNotExist:
        data12 = None
        
    try: 
        data1 = IPMT_Form_model_submitted_1.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_1.DoesNotExist:
        data1 = None

    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Remarks.DoesNotExist:
        data = None
        
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    data7 = None
    data8 = None
    data9 = None
    
    context = {
        'data1': data1,
        'data2' : data2,
        'data3' : data3,
        'data4' : data4,
        'data5' : data5,
        'data6' : data6,
        'data7' : data7,
        'data8' : data8,
        'data9' : data9,
        'data10' : data10,
        'data11' : data11,
        'data12' : data12,
        'data' : data
    }

    return render(request, 'downloads/IPMTForm.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_secondmidsem_ViewIPMT(request):
    current_year = datetime.now().year
    actual_year = current_year - 1
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_day = 5
    
    secondmidsem_date = datetime(actual_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    
    try: 
        data2 = IPMT_Form_model_submitted_2.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_2.DoesNotExist:
        data2 = None

    try: 
        data3 = IPMT_Form_model_submitted_3.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_3.DoesNotExist:
        data3 = None
    
    try: 
        data4 = IPMT_Form_model_submitted_4.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_4.DoesNotExist:
        data4 = None

    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None
        
    data1 = None        
    data5 = None
    data6 = None
    data7 = None
    data8 = None
    data9 = None
    data10 = None
    data11 = None
    data12 = None
    
    context = {
        'data1': data1,
        'data2' : data2,
        'data3' : data3,
        'data4' : data4,
        'data5' : data5,
        'data6' : data6,
        'data7' : data7,
        'data8' : data8,
        'data9' : data9,
        'data10' : data10,
        'data11' : data11,
        'data12' : data12,
        'data' : data
    }

    return render(request, 'downloads/IPCRForm.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_secondfinalsem_ViewIPMT(request):
    current_year = datetime.now().year
    actual_year = current_year - 1
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(actual_year, secondsem_endmonth, secondsem_day).date()
    
    try: 
        data4 = IPMT_Form_model_submitted_4.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_4.DoesNotExist:
        data4 = None

    try: 
        data5 = IPMT_Form_model_submitted_5.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_5.DoesNotExist:
        data5 = None

    try: 
        data6 = IPMT_Form_model_submitted_6.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_6.DoesNotExist:
        data6 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Remarks.DoesNotExist:
        data = None
    
    
    data1 = None
    data2 = None
    data3 = None
    data7 = None
    data8 = None
    data9 = None
    data10 = None
    data11 = None
    data12 = None
    
    context = {
        'data1': data1,
        'data2' : data2,
        'data3' : data3,
        'data4' : data4,
        'data5' : data5,
        'data6' : data6,
        'data7' : data7,
        'data8' : data8,
        'data9' : data9,
        'data10' : data10,
        'data11' : data11,
        'data12' : data12,
        'data' : data
    }

    return render(request, 'downloads/IPMTForm.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_firstmidsem_DownloadIPMT(request):
    current_year = datetime.now().year
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 8 and current_month <= 10:
        actual_year = current_year - 1
    else:
        actual_year = current_year - 2
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    
    try: 
        data8 = IPMT_Form_model_submitted_8.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_8.DoesNotExist:
        data8 = None
        
    try: 
        data9 = IPMT_Form_model_submitted_9.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_9.DoesNotExist:
        data9 = None
        
    try: 
        data10 = IPMT_Form_model_submitted_10.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_10.DoesNotExist:
        data10 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None    
        
    data1 = None
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    data7 = None
    data11 = None
    data12 = None
    
    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target003.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    
    
    template = get_template('downloads/IPMTForm_Download.html')
    html_content = template.render({'data1': data1,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'data4' : data4,
                                    'data5' : data5,
                                    'data6' : data6,
                                    'data7' : data7,
                                    'data8' : data8,
                                    'data9' : data9,
                                    'data10' : data10,
                                    'data11' : data11,
                                    'data12' : data12,
                                    'data' : data,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    }
                                    ,request)

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
        'orientation': 'Landscape'
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPMTForm_FirstSemMidTerm.pdf"'
    return response

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_firstfinalsem_DownloadIPMT(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 10 and current_month <= 12:
        actual_year = current_year - 1
        actual_actual_year = current_year
    else:
        actual_year = current_year - 2
        actual_actual_year = current_year - 1
    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25

    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(actual_actual_year, firstsem_endmonth, firstsem_day).date()
    
    try: 
        data8 = IPMT_Form_model_submitted_8.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_8.DoesNotExist:
        data8 = None
        
    try: 
        data9 = IPMT_Form_model_submitted_9.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_9.DoesNotExist:
        data9 = None
        
    try: 
        data10 = IPMT_Form_model_submitted_10.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_10.DoesNotExist:
        data10 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Remarks.DoesNotExist:
        data = None    
        
    data1 = None
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    data7 = None
    data11 = None
    data12 = None
    
    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target003.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    
    
    template = get_template('downloads/IPMTForm_Download.html')
    html_content = template.render({'data1': data1,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'data4' : data4,
                                    'data5' : data5,
                                    'data6' : data6,
                                    'data7' : data7,
                                    'data8' : data8,
                                    'data9' : data9,
                                    'data10' : data10,
                                    'data11' : data11,
                                    'data12' : data12,
                                    'data' : data,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    }
                                    ,request)

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
        'orientation': 'Landscape'
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPMTForm_FirstSemFinalTerm.pdf"'
    return response

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_secondmidsem_DownloadIPMT(request):
    current_year = datetime.now().year
    actual_year = current_year - 1
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_day = 5
    
    secondmidsem_date = datetime(actual_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    
    try: 
        data2 = IPMT_Form_model_submitted_2.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_2.DoesNotExist:
        data2 = None

    try: 
        data3 = IPMT_Form_model_submitted_3.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_3.DoesNotExist:
        data3 = None
    
    try: 
        data4 = IPMT_Form_model_submitted_4.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_4.DoesNotExist:
        data4 = None

    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None
        
    data1 = None        
    data5 = None
    data6 = None
    data7 = None
    data8 = None
    data9 = None
    data10 = None
    data11 = None
    data12 = None
    
    
    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target003.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    
    
    template = get_template('downloads/IPMTForm_Download.html')
    html_content = template.render({'data1': data1,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'data4' : data4,
                                    'data5' : data5,
                                    'data6' : data6,
                                    'data7' : data7,
                                    'data8' : data8,
                                    'data9' : data9,
                                    'data10' : data10,
                                    'data11' : data11,
                                    'data12' : data12,
                                    'data' : data,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    }
                                    ,request)

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
        'orientation': 'Landscape'
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPMTForm_SecondSemMidTerm.pdf"'
    return response

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_secondfinalsem_DownloadIPMT(request):
    current_year = datetime.now().year
    actual_year = current_year - 1
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(actual_year, secondsem_endmonth, secondsem_day).date()
    
    try: 
        data4 = IPMT_Form_model_submitted_4.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_4.DoesNotExist:
        data4 = None

    try: 
        data5 = IPMT_Form_model_submitted_5.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_5.DoesNotExist:
        data5 = None

    try: 
        data6 = IPMT_Form_model_submitted_6.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_6.DoesNotExist:
        data6 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Remarks.DoesNotExist:
        data = None
    
    
    data1 = None
    data2 = None
    data3 = None
    data7 = None
    data8 = None
    data9 = None
    data10 = None
    data11 = None
    data12 = None
    
    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target003.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    
    
    template = get_template('downloads/IPMTForm_Download.html')
    html_content = template.render({'data1': data1,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'data4' : data4,
                                    'data5' : data5,
                                    'data6' : data6,
                                    'data7' : data7,
                                    'data8' : data8,
                                    'data9' : data9,
                                    'data10' : data10,
                                    'data11' : data11,
                                    'data12' : data12,
                                    'data' : data,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    }
                                    ,request)

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
        'orientation': 'Landscape'
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPMTForm_SecondSemFinalTerm.pdf"'
    return response

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_last_firstmidsem_ViewIPMT(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 8 and current_month <= 10:
        actual_year = current_year - 2
    else:
        actual_year = current_year - 3
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    try: 
        data8 = IPMT_Form_model_submitted_8.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_8.DoesNotExist:
        data8 = None
        
    try: 
        data9 = IPMT_Form_model_submitted_9.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_9.DoesNotExist:
        data9 = None
        
    try: 
        data10 = IPMT_Form_model_submitted_10.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_10.DoesNotExist:
        data10 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None    
        
    data1 = None
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    data7 = None
    data11 = None
    data12 = None
    
    context = {
        'data1': data1,
        'data2' : data2,
        'data3' : data3,
        'data4' : data4,
        'data5' : data5,
        'data6' : data6,
        'data7' : data7,
        'data8' : data8,
        'data9' : data9,
        'data10' : data10,
        'data11' : data11,
        'data12' : data12,
        'data' : data
    }
    return render(request, 'downloads/IPMTForm.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_last_firstfinalsem_ViewIPMT(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 10 and current_month <= 12:
        actual_year = current_year - 2
        actual_actual_year = current_year - 1
    else:
        actual_year = current_year - 3
        actual_actual_year = current_year - 2
    actual_year = current_year - 3
    actual_actual_year = current_year - 2
    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25

    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(actual_actual_year, firstsem_endmonth, firstsem_day).date()
    
    
    try: 
        data10 = IPMT_Form_model_submitted_10.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_10.DoesNotExist:
        data10 = None

    try: 
        data11 = IPMT_Form_model_submitted_11.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_11.DoesNotExist:
        data11 = None
    
    try: 
        data12 = IPMT_Form_model_submitted_12.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_12.DoesNotExist:
        data12 = None
        
    try: 
        data1 = IPMT_Form_model_submitted_1.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_1.DoesNotExist:
        data1 = None

    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Remarks.DoesNotExist:
        data = None
        
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    data7 = None
    data8 = None
    data9 = None
    
    context = {
        'data1': data1,
        'data2' : data2,
        'data3' : data3,
        'data4' : data4,
        'data5' : data5,
        'data6' : data6,
        'data7' : data7,
        'data8' : data8,
        'data9' : data9,
        'data10' : data10,
        'data11' : data11,
        'data12' : data12,
        'data' : data
    }

    return render(request, 'downloads/IPMTForm.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_last_secondmidsem_ViewIPMT(request):
    current_year = datetime.now().year
    actual_year = current_year - 2
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_day = 5
    
    secondmidsem_date = datetime(actual_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    
    try: 
        data2 = IPMT_Form_model_submitted_2.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_2.DoesNotExist:
        data2 = None

    try: 
        data3 = IPMT_Form_model_submitted_3.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_3.DoesNotExist:
        data3 = None
    
    try: 
        data4 = IPMT_Form_model_submitted_4.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_4.DoesNotExist:
        data4 = None

    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None
        
    data1 = None        
    data5 = None
    data6 = None
    data7 = None
    data8 = None
    data9 = None
    data10 = None
    data11 = None
    data12 = None
    
    context = {
        'data1': data1,
        'data2' : data2,
        'data3' : data3,
        'data4' : data4,
        'data5' : data5,
        'data6' : data6,
        'data7' : data7,
        'data8' : data8,
        'data9' : data9,
        'data10' : data10,
        'data11' : data11,
        'data12' : data12,
        'data' : data
    }

    return render(request, 'downloads/IPCRForm.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_last_secondfinalsem_ViewIPMT(request):
    current_year = datetime.now().year
    actual_year = current_year - 2
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(actual_year, secondsem_endmonth, secondsem_day).date()
    
    try: 
        data4 = IPMT_Form_model_submitted_4.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_4.DoesNotExist:
        data4 = None

    try: 
        data5 = IPMT_Form_model_submitted_5.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_5.DoesNotExist:
        data5 = None

    try: 
        data6 = IPMT_Form_model_submitted_6.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_6.DoesNotExist:
        data6 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Remarks.DoesNotExist:
        data = None
    
    
    data1 = None
    data2 = None
    data3 = None
    data7 = None
    data8 = None
    data9 = None
    data10 = None
    data11 = None
    data12 = None
    
    context = {
        'data1': data1,
        'data2' : data2,
        'data3' : data3,
        'data4' : data4,
        'data5' : data5,
        'data6' : data6,
        'data7' : data7,
        'data8' : data8,
        'data9' : data9,
        'data10' : data10,
        'data11' : data11,
        'data12' : data12,
        'data' : data
    }

    return render(request, 'downloads/IPMTForm.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_last_firstmidsem_DownloadIPMT(request):
    current_year = datetime.now().year
    actual_year = current_year - 3
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_day = 25
    firstmidsem_date = datetime(actual_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    
    try: 
        data8 = IPMT_Form_model_submitted_8.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_8.DoesNotExist:
        data8 = None
        
    try: 
        data9 = IPMT_Form_model_submitted_9.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_9.DoesNotExist:
        data9 = None
        
    try: 
        data10 = IPMT_Form_model_submitted_10.objects.get(author=request.user, IPCR_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Form_model_submitted_10.DoesNotExist:
        data10 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(firstmidsem_date, firstfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None    
        
    data1 = None
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    data7 = None
    data11 = None
    data12 = None
    
    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target003.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    
    
    template = get_template('downloads/IPMTForm_Download.html')
    html_content = template.render({'data1': data1,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'data4' : data4,
                                    'data5' : data5,
                                    'data6' : data6,
                                    'data7' : data7,
                                    'data8' : data8,
                                    'data9' : data9,
                                    'data10' : data10,
                                    'data11' : data11,
                                    'data12' : data12,
                                    'data' : data,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    }
                                    ,request)

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
        'orientation': 'Landscape'
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPMTForm_FirstSemMidTerm.pdf"'
    return response

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_last_firstfinalsem_DownloadIPMT(request):
    current_year = datetime.now().year
    actual_year = current_year - 3
    actual_actual_year = current_year - 2
    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25

    firstfinalsem_date = datetime(actual_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(actual_actual_year, firstsem_endmonth, firstsem_day).date()
    
    try: 
        data8 = IPMT_Form_model_submitted_8.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_8.DoesNotExist:
        data8 = None
        
    try: 
        data9 = IPMT_Form_model_submitted_9.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_9.DoesNotExist:
        data9 = None
        
    try: 
        data10 = IPMT_Form_model_submitted_10.objects.get(author=request.user, IPCR_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Form_model_submitted_10.DoesNotExist:
        data10 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(firstfinalsem_date, firstsem_enddate))
    except IPMT_Remarks.DoesNotExist:
        data = None    
        
    data1 = None
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    data7 = None
    data11 = None
    data12 = None
    
    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target003.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    
    
    template = get_template('downloads/IPMTForm_Download.html')
    html_content = template.render({'data1': data1,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'data4' : data4,
                                    'data5' : data5,
                                    'data6' : data6,
                                    'data7' : data7,
                                    'data8' : data8,
                                    'data9' : data9,
                                    'data10' : data10,
                                    'data11' : data11,
                                    'data12' : data12,
                                    'data' : data,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    }
                                    ,request)

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
        'orientation': 'Landscape'
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPMTForm_FirstSemFinalTerm.pdf"'
    return response

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_last_secondmidsem_DownloadIPMT(request):
    current_year = datetime.now().year
    actual_year = current_year - 2
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_day = 5
    
    secondmidsem_date = datetime(actual_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    
    try: 
        data2 = IPMT_Form_model_submitted_2.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_2.DoesNotExist:
        data2 = None

    try: 
        data3 = IPMT_Form_model_submitted_3.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_3.DoesNotExist:
        data3 = None
    
    try: 
        data4 = IPMT_Form_model_submitted_4.objects.get(author=request.user, IPCR_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Form_model_submitted_4.DoesNotExist:
        data4 = None

    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(secondmidsem_date, secondfinalsem_date))
    except IPMT_Remarks.DoesNotExist:
        data = None
        
    data1 = None        
    data5 = None
    data6 = None
    data7 = None
    data8 = None
    data9 = None
    data10 = None
    data11 = None
    data12 = None
    
    
    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target003.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    
    
    template = get_template('downloads/IPMTForm_Download.html')
    html_content = template.render({'data1': data1,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'data4' : data4,
                                    'data5' : data5,
                                    'data6' : data6,
                                    'data7' : data7,
                                    'data8' : data8,
                                    'data9' : data9,
                                    'data10' : data10,
                                    'data11' : data11,
                                    'data12' : data12,
                                    'data' : data,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    }
                                    ,request)

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
        'orientation': 'Landscape'
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPMTForm_SecondSemMidTerm.pdf"'
    return response

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def last_last_secondfinalsem_DownloadIPMT(request):
    current_year = datetime.now().year
    actual_year = current_year - 2
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    secondfinalsem_date = datetime(actual_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(actual_year, secondsem_endmonth, secondsem_day).date()
    
    try: 
        data4 = IPMT_Form_model_submitted_4.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_4.DoesNotExist:
        data4 = None

    try: 
        data5 = IPMT_Form_model_submitted_5.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_5.DoesNotExist:
        data5 = None

    try: 
        data6 = IPMT_Form_model_submitted_6.objects.get(author=request.user, IPCR_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Form_model_submitted_6.DoesNotExist:
        data6 = None
    
    try: 
        data = IPMT_Remarks.objects.get(author=request.user, IPMT_Submitted__range=(secondfinalsem_date, secondsem_enddate))
    except IPMT_Remarks.DoesNotExist:
        data = None
    
    
    data1 = None
    data2 = None
    data3 = None
    data7 = None
    data8 = None
    data9 = None
    data10 = None
    data11 = None
    data12 = None
    
    image_paths = [r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target001.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target002.png', 
                   r'C:\Users\Admin\Downloads\IPCR_System\static\IPMT\target003.png']
    base64_string1 = image_to_base64(image_paths[0])
    base64_string2 = image_to_base64(image_paths[1])
    base64_string3 = image_to_base64(image_paths[2])
    
    
    template = get_template('downloads/IPMTForm_Download.html')
    html_content = template.render({'data1': data1,
                                    'data2' : data2,
                                    'data3' : data3,
                                    'data4' : data4,
                                    'data5' : data5,
                                    'data6' : data6,
                                    'data7' : data7,
                                    'data8' : data8,
                                    'data9' : data9,
                                    'data10' : data10,
                                    'data11' : data11,
                                    'data12' : data12,
                                    'data' : data,
                                    'base64_string1': base64_string1,
                                    'base64_string2': base64_string2,
                                    'base64_string3': base64_string3,
                                    }
                                    ,request)

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
        'orientation': 'Landscape'
    }

    pdf_file = pdfkit.from_string(html_content, False, options=options, configuration=pdfkit_config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="IPMTForm_SecondSemFinalTerm.pdf"'
    return response
