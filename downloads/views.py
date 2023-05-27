from django.shortcuts import render
from forms.forms import *
from forms.models import *


# Create your views here.
def download(request):
    return render(request, ('downloads/IPCR_Download.html'))

def Show_IPCR(request):
    
    return render (request, ('downloads/IPCRForm_View.html'))

