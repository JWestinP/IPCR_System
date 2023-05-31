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



# Create your views here.
def download(request):
    return render(request, ('downloads/IPCR_Download.html'))

@allowed_users(allowed_roles=['Member'])
def Show_IPCR(request):
    try: 
        data = IPCR_Form_model_submitted.objects.get(author=request.user)
    except IPCR_Form_model_submitted.DoesNotExist:
        data = None

    try:
        data2 = IPCR_Remarks.objects.get(author = request.user)
    except IPCR_Remarks.DoesNotExist:
        data2 = None
    
    try: 
        data3 = IPCR_Rating.objects.get(author=request.user)
    except IPCR_Rating.DoesNotExist:
        data3 = None

    context = {
        'data': data,
        'data2' : data2,
        'data3' : data3
    }

    return render(request, 'downloads/IPCRForm.html', context)

def image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

@allowed_users(allowed_roles=['Member'])
def download_pdf(request):
    data = IPCR_Form_model_submitted.objects.get(author=request.user)

    image_path = r'C:\Users\Admin\Downloads\IPCR_System\static\IPCR\target001.png'
    image_base64 = image_to_base64(image_path)
    
    template = get_template('downloads/IPCRForm_Download.html')
    html_content = template.render({'data': data, 'image_base64': image_base64}, request)

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
    response['Content-Disposition'] = 'attachment; filename="IPCRForm.pdf"'
    return response

