from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
from forms.forms import *
from forms.models import *
from django.db.models import Sum
from datetime import date, datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = 'login')
def dashboard (request):
    return render(request, ('dashboard/dashboard.html'))

@login_required(login_url = 'login')
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/dashboard.html')
    
@login_required(login_url = 'login')
class ChartData(APIView):
    
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):
        current_SY1 = datetime.now().year
        current_SY2 = current_SY1 - 1
        firstmidsem_month = 8
        firstsem_day = 25
        secondsem_endmonth = 6
        secondsem_day = 5
        firstmidsem_date = datetime(current_SY2, firstmidsem_month, firstsem_day).date()
        secondsem_enddate = datetime(current_SY1, secondsem_endmonth, secondsem_day).date()
        try:
            group = Group.objects.get(name="CAS_Faculty")
            users = group.user_set.all()
            CAS_instances = IPCR_Form_model_submitted.objects.filter(author__in=users, IPCR_Submitted__range=(firstmidsem_date, secondsem_enddate))
            CAS_research_total = CAS_instances.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
            CAS_submitted_total = CAS_instances.count()
        except Group.DoesNotExist:
            CAS_instances = []
            
        try:
            group = Group.objects.get(name="CBA_Faculty")
            users = group.user_set.all()
            CBA_instances = IPCR_Form_model_submitted.objects.filter(author__in=users, IPCR_Submitted__range=(firstmidsem_date, secondsem_enddate))
            CBA_research_total = CBA_instances.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
            CBA_submitted_total = CBA_instances.count()
        except Group.DoesNotExist:
            CBA_instances = []
        
        try:
            group = Group.objects.get(name="CCJE_Faculty")
            users = group.user_set.all()
            CCJE_instances = IPCR_Form_model_submitted.objects.filter(author__in=users, IPCR_Submitted__range=(firstmidsem_date, secondsem_enddate))
            CCJE_research_total = CCJE_instances.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
            CCJE_submitted_total = CCJE_instances.count()
        except Group.DoesNotExist:
            CCJE_instances = []
            
        try:
            group = Group.objects.get(name="CCS_Faculty")
            users = group.user_set.all()
            CCS_instances = IPCR_Form_model_submitted.objects.filter(author__in=users, IPCR_Submitted__range=(firstmidsem_date, secondsem_enddate))
            CCS_research_total = CCS_instances.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
            CCS_submitted_total = CCS_instances.count()
        except Group.DoesNotExist:
            CCS_instances = []
            
        try:
            group = Group.objects.get(name="CHMT_Faculty")
            users = group.user_set.all()
            CHMT_instances = IPCR_Form_model_submitted.objects.filter(author__in=users, IPCR_Submitted__range=(firstmidsem_date, secondsem_enddate))
            CHMT_research_total = CHMT_instances.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
            CHMT_submitted_total = CHMT_instances.count()
        except Group.DoesNotExist:
            CHMT_instances = []
            
        try:
            group = Group.objects.get(name="CIT_Faculty")
            users = group.user_set.all()
            CIT_instances = IPCR_Form_model_submitted.objects.filter(author__in=users, IPCR_Submitted__range=(firstmidsem_date, secondsem_enddate))
            CIT_research_total = CIT_instances.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
            CIT_submitted_total = CIT_instances.count()
        except Group.DoesNotExist:
            CIT_instances = []
            
        try:
            group = Group.objects.get(name="COE_Faculty")
            users = group.user_set.all()
            COE_instances = IPCR_Form_model_submitted.objects.filter(author__in=users, IPCR_Submitted__range=(firstmidsem_date, secondsem_enddate))
            COE_research_total = COE_instances.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
            COE_submitted_total = COE_instances.count()
        except Group.DoesNotExist:
            COE_instances = []
            
        labels = [
            'CAS',
            'CBA', 
            'CCJE', 
            'CCS', 
            'CHMT', 
            'CIT', 
            'COE'
            ]
        chartLabel = "IPCR Total Research Published"
        chartdata = [CAS_research_total, CBA_research_total, CCJE_research_total, CCS_research_total, CHMT_research_total,
                     CIT_research_total, COE_research_total]
        
        IPCR_Submitted_labels = [
            'CAS',
            'CBA', 
            'CCJE', 
            'CCS', 
            'CHMT', 
            'CIT', 
            'COE'
            ]
        IPCR_Submitted_chartLabel = "IPCR Total Submitted"
        IPCR_Submitted_chartdata = [CAS_submitted_total, CBA_submitted_total, CCJE_submitted_total, CCS_submitted_total, CHMT_submitted_total,
                     CIT_submitted_total, COE_submitted_total]
        data ={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
                     "IPCR_Submitted_labels":IPCR_Submitted_labels,
                     "IPCR_Submitted_chartLabel":IPCR_Submitted_chartLabel,
                     "IPCR_Submitted_chartdata":IPCR_Submitted_chartdata,
             }
        return Response(data)    