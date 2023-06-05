from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date, datetime
from django.forms import modelform_factory
from django.db.models import Sum
from home.decorators import allowed_users
import random
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def IPCR_Form(request):
    current_user = request.user
    IPCRForm = modelform_factory(IPCR_Form_model, fields="__all__", exclude=['author', 'department', 'IPCR_Saved', 'IPCR_Deadline', 'approver'])
    current_date = datetime.now().date()
    current_year = datetime.now().year
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    firstmidsem_date = datetime(current_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(current_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(current_year, firstsem_endmonth, firstsem_day).date()
    
    secondmidsem_date = datetime(current_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(current_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(current_year, secondsem_endmonth, secondsem_day).date()

    try:
        existing_instance = IPCR_Form_model.objects.filter(author=request.user).order_by('-IPCR_Saved').first()
    except IPCR_Form_model.DoesNotExist:
        existing_instance = None

    #Conditional statements for checking the date and creating a new IPCR form if ever a specific date has passed
    if existing_instance:
        if current_date >= firstmidsem_date and current_date <= firstfinalsem_date:
            if existing_instance and existing_instance.IPCR_Saved and existing_instance.IPCR_Saved >= firstmidsem_date and existing_instance.IPCR_Saved <= firstfinalsem_date:
                existing_instance = IPCR_Form_model.objects.filter(author=request.user).order_by('-IPCR_Saved').first()
            else:
                existing_instance = None

        elif current_date >= firstfinalsem_date and current_date <= firstsem_enddate:
            if existing_instance and existing_instance.IPCR_Saved and existing_instance.IPCR_Saved >= firstfinalsem_date and existing_instance.IPCR_Saved <= firstsem_enddate:
                existing_instance = IPCR_Form_model.objects.filter(author=request.user).order_by('-IPCR_Saved').first()
            else:
                existing_instance = None

        elif current_date >= secondmidsem_date and current_date <= secondfinalsem_date:
            if existing_instance and existing_instance.IPCR_Saved and existing_instance.IPCR_Saved >= secondmidsem_date and existing_instance.IPCR_Saved <= secondfinalsem_date:
                existing_instance = IPCR_Form_model.objects.filter(author=request.user).order_by('-IPCR_Saved').first()
            else:
                existing_instance = None

        elif current_date >= secondfinalsem_date and current_date <= secondsem_enddate:
            if existing_instance and existing_instance.IPCR_Saved and existing_instance.IPCR_Saved >= secondfinalsem_date and existing_instance.IPCR_Saved <= secondsem_enddate:
                existing_instance = IPCR_Form_model.objects.filter(author=request.user).order_by('-IPCR_Saved').first()
            else:
                existing_instance = None
    
    #Instantiate the form for handling user input           
    if request.method == 'POST':
        forms = IPCRForm(request.POST, instance=existing_instance)
        if forms.is_valid():
            current_user = request.user
            group_names = [group.name for group in current_user.groups.all()]
            model_instance = forms.save(commit=False)
            model_instance.author = current_user
            model_instance.IPCR_Saved = current_date
            model_instance.department = ', '.join(group_names)
            
            if current_date <= secondsem_enddate:
                model_instance.IPCR_Deadline = secondsem_enddate
                model_instance.save()

            elif current_date <= firstfinalsem_date:
                model_instance.IPCR_Deadline = firstfinalsem_date
                model_instance.save()

            elif current_date <= firstsem_enddate:
                model_instance.IPCR_Deadline = firstsem_enddate
                model_instance.save()

            elif current_date <= secondfinalsem_date:
                model_instance.IPCR_Deadline = secondfinalsem_date
                model_instance.save()  
                
            model_instance.save()
            
            #Handling the gathering of IPMT data
            try:
                existing_instance = IPMT_Form_model.objects.filter(author=request.user).order_by('-IPCR_Saved').first()
            except IPMT_Form_model.DoesNotExist:
                existing_instance = None

            if existing_instance:
                if current_date >= firstmidsem_date and current_date <= firstfinalsem_date:
                    if existing_instance and existing_instance.IPCR_Saved and existing_instance.IPCR_Saved >= firstmidsem_date and existing_instance.IPCR_Saved <= firstfinalsem_date:
                        existing_instance = "Exists"
                    else:
                        existing_instance = None

                elif current_date >= firstfinalsem_date and current_date <= firstsem_enddate:
                    if existing_instance and existing_instance.IPCR_Saved and existing_instance.IPCR_Saved >= firstfinalsem_date and existing_instance.IPCR_Saved <= firstsem_enddate:
                        existing_instance = "Exists"
                    else:
                        existing_instance = None

                elif current_date >= secondmidsem_date and current_date <= secondfinalsem_date:
                    if existing_instance and existing_instance.IPCR_Saved and existing_instance.IPCR_Saved >= secondmidsem_date and existing_instance.IPCR_Saved <= secondfinalsem_date:
                        existing_instance = "Exists"
                    else:
                        existing_instance = None

                elif current_date >= secondfinalsem_date and current_date <= secondsem_enddate:
                    if existing_instance and existing_instance.IPCR_Saved and existing_instance.IPCR_Saved >= secondfinalsem_date and existing_instance.IPCR_Saved <= secondsem_enddate:
                        existing_instance = "Exists"
                    else:
                        existing_instance = None
            
            #Generate a new model instance for IPMT if it doesn't exist yet      
            if existing_instance == None:
                source_instance = IPCR_Form_model.objects.filter(author=request.user).order_by('-IPCR_Saved').first()
                destination_instance = IPMT_Form_model.objects.create(author = request.user)
                destination_instance.syllabus_Accomplished = source_instance.syllabus_Accomplished
                destination_instance.CourseGuide_Accomplished = source_instance.CourseGuide_Accomplished
                destination_instance.SLM_Accomplished = source_instance.SLM_Accomplished
                destination_instance.SubjectAreas_Accomplished = source_instance.SubjectAreas_Accomplished
                destination_instance.AttendanceSheet_Accomplished = source_instance.AttendanceSheet_Accomplished
                destination_instance.ClassRecord_Accomplished = source_instance.ClassRecord_Accomplished
                destination_instance.TeachingEffectiveness_Accomplished = source_instance.TeachingEffectiveness_Accomplished
                destination_instance.ClassroomObservation_Accomplished = source_instance.ClassroomObservation_Accomplished
                destination_instance.TOSRubrics_Accomplished = source_instance.MidtermTOSRubrics_Accomplished + source_instance.FinaltermTOSRubrics_Accomplished
                destination_instance.TestQuestions_Accomplished = source_instance.MidtermTestQuestions_Accomplished + source_instance.FinaltermTestQuestions_Accomplished
                destination_instance.AnswerKey_Accomplished = source_instance.MidtermAnswerKey_Accomplished + source_instance.FinaltermAnswerKey_Accomplished
                destination_instance.GradingSheet_Accomplished = source_instance.GradingSheet_Accomplished
                destination_instance.StudentAdviced_Accomplished = source_instance.StudentAdviced_Accomplished
                destination_instance.AccomplishmentReport_Accomplished = source_instance.AccomplishmentReport_Accomplished
                destination_instance.ResearchProposalSubmitted_Accomplished = source_instance.ResearchProposalSubmitted_Accomplished
                destination_instance.ResearchImplemented_Accomplished = source_instance.ResearchImplemented_Accomplished
                destination_instance.ResearchPresented_Accomplished = source_instance.ResearchPresented_Accomplished
                destination_instance.ResearchPublished_Accomplished = source_instance.ResearchPublished_Accomplished
                destination_instance.ApprovedIPRights_Accomplished = source_instance.ApprovedIPRights_Accomplished
                destination_instance.ResearchUtilized_Accomplished = source_instance.ResearchUtilized_Accomplished
                destination_instance.NumberOfCitations_Accomplished = source_instance.NumberOfCitations_Accomplished
                destination_instance.ExtensionProposalSubmitted_Accomplished = source_instance.ExtensionProposalSubmitted_Accomplished
                destination_instance.PersonTrained_Accomplished = source_instance.PersonTrained_Accomplished
                destination_instance.PersonAvailedRatedGood_Accomplished = source_instance.PersonAvailedRatedGood_Accomplished           
                destination_instance.PersonTrainedRatedGood_Accomplished = source_instance.PersonTrainedRatedGood_Accomplished
                destination_instance.TechnicalAdvice_Accomplished = source_instance.TechnicalAdvice_Accomplished
                destination_instance.AccomplishmentReportDeligatedAssignment_Accomplished = source_instance.AccomplishmentReportDeligatedAssignment_Accomplished
                destination_instance.FlagRaisingAttendance_Accomplished = source_instance.FlagRaisingAttendance_Accomplished
                destination_instance.FlagLoweringAttendance_Accomplished = source_instance.FlagLoweringAttendance_Accomplished
                destination_instance.WellnessProgramAttendance_Accomplished = source_instance.WellnessProgramAttendance_Accomplished
                destination_instance.SchoolCelebrationAttendance_Accomplished = source_instance.SchoolCelebrationAttendance_Accomplished
                destination_instance.TrainingAttendance_Accomplished = source_instance.TrainingAttendance_Accomplished
                destination_instance.FacultyMeetingAttendance_Accomplished = source_instance.FacultyMeetingAttendance_Accomplished
                destination_instance.AccreditationAttendance_Accomplished = source_instance.AccreditationAttendance_Accomplished
                destination_instance.SpiritualActivityAttendance_Accomplished = source_instance.SpiritualActivityAttendance_Accomplished
                destination_instance.IPCR_Saved = date.today()
                
                destination_instance.save()
            
            #Getting the existing instance of IPMT and getting the total accomplished number per field
            else:
                if current_date >= firstmidsem_date and current_date <= firstfinalsem_date:
                    firstmidterm_instance = IPMT_Form_model.objects.filter(author = request.user, IPCR_Saved__range=(firstmidsem_date, firstfinalsem_date))
                    total_IPCR = firstmidterm_instance.aggregate(
                        total_syllabus = Sum('syllabus_Accomplished'),
                        total_courseguide = Sum('CourseGuide_Accomplished'),
                        total_SLM = Sum('SLM_Accomplished'),
                        total_SubjectAreas = Sum('SubjectAreas_Accomplished'),
                        total_AttendanceSheet = Sum('AttendanceSheet_Accomplished'),
                        total_ClassRecord = Sum('ClassRecord_Accomplished'),
                        total_TeachingEffectiveness = Sum('TeachingEffectiveness_Accomplished'),
                        total_ClassroomObservation = Sum('ClassroomObservation_Accomplished'),
                        total_TOSRubrics = Sum('TOSRubrics_Accomplished'),
                        total_TestQuestions = Sum('TestQuestions_Accomplished'),
                        total_AnswerKey = Sum('AnswerKey_Accomplished'),
                        total_GradingSheet = Sum('GradingSheet_Accomplished'),
                        total_StudentAdviced = Sum('StudentAdviced_Accomplished'),
                        total_AccomplishmentReport = Sum('AccomplishmentReport_Accomplished'),
                        total_ResearchProposalSubmitted = Sum('ResearchProposalSubmitted_Accomplished'),
                        total_ResearchImplemented = Sum('ResearchImplemented_Accomplished'),
                        total_ResearchPresented = Sum('ResearchPresented_Accomplished'),
                        total_ResearchPublished = Sum('ResearchPublished_Accomplished'),
                        total_ApprovedIPRights = Sum('ApprovedIPRights_Accomplished'),
                        total_ResearchUtilized = Sum('ResearchUtilized_Accomplished'),
                        total_NumberOfCitations = Sum('NumberOfCitations_Accomplished'),
                        total_ExtensionProposalSubmitted = Sum('ExtensionProposalSubmitted_Accomplished'),
                        total_PersonTrained = Sum('PersonTrained_Accomplished'),
                        total_PersonAvailedRatedGood = Sum('PersonAvailedRatedGood_Accomplished'),
                        total_PersonTrainedRatedGood = Sum('PersonTrainedRatedGood_Accomplished'),
                        total_TechnicalAdvice = Sum('TechnicalAdvice_Accomplished'),
                        total_AccomplishmentReportDeligatedAssignment = Sum('AccomplishmentReportDeligatedAssignment_Accomplished'),
                        total_FlagRaisingAttendance = Sum('FlagRaisingAttendance_Accomplished'),
                        total_FlagLoweringAttendance = Sum('FlagLoweringAttendance_Accomplished'),
                        total_WellnessProgramAttendance = Sum('WellnessProgramAttendance_Accomplished'),
                        total_SchoolCelebrationAttendance = Sum('SchoolCelebrationAttendance_Accomplished'),
                        total_TrainingAttendance = Sum('TrainingAttendance_Accomplished'),
                        total_FacultyMeetingAttendance = Sum('FacultyMeetingAttendance_Accomplished'),
                        total_AccreditationAttendance = Sum('AccreditationAttendance_Accomplished'),
                        total_SpiritualActivityAttendance = Sum('SpiritualActivityAttendance_Accomplished')
                    )
                
                elif current_date >= firstfinalsem_date and current_date <= firstsem_enddate:
                    firstfinalterm_instance = IPMT_Form_model.objects.filter(author = request.user, IPCR_Saved__range=(firstfinalsem_date, firstsem_enddate))
                    total_IPCR = firstfinalterm_instance.aggregate(
                        total_syllabus = Sum('syllabus_Accomplished'),
                        total_courseguide = Sum('CourseGuide_Accomplished'),
                        total_SLM = Sum('SLM_Accomplished'),
                        total_SubjectAreas = Sum('SubjectAreas_Accomplished'),
                        total_AttendanceSheet = Sum('AttendanceSheet_Accomplished'),
                        total_ClassRecord = Sum('ClassRecord_Accomplished'),
                        total_TeachingEffectiveness = Sum('TeachingEffectiveness_Accomplished'),
                        total_ClassroomObservation = Sum('ClassroomObservation_Accomplished'),
                        total_TOSRubrics = Sum('TOSRubrics_Accomplished'),
                        total_TestQuestions = Sum('TestQuestions_Accomplished'),
                        total_AnswerKey = Sum('AnswerKey_Accomplished'),
                        total_GradingSheet = Sum('GradingSheet_Accomplished'),
                        total_StudentAdviced = Sum('StudentAdviced_Accomplished'),
                        total_AccomplishmentReport = Sum('AccomplishmentReport_Accomplished'),
                        total_ResearchProposalSubmitted = Sum('ResearchProposalSubmitted_Accomplished'),
                        total_ResearchImplemented = Sum('ResearchImplemented_Accomplished'),
                        total_ResearchPresented = Sum('ResearchPresented_Accomplished'),
                        total_ResearchPublished = Sum('ResearchPublished_Accomplished'),
                        total_ApprovedIPRights = Sum('ApprovedIPRights_Accomplished'),
                        total_ResearchUtilized = Sum('ResearchUtilized_Accomplished'),
                        total_NumberOfCitations = Sum('NumberOfCitations_Accomplished'),
                        total_ExtensionProposalSubmitted = Sum('ExtensionProposalSubmitted_Accomplished'),
                        total_PersonTrained = Sum('PersonTrained_Accomplished'),
                        total_PersonAvailedRatedGood = Sum('PersonAvailedRatedGood_Accomplished'),
                        total_PersonTrainedRatedGood = Sum('PersonTrainedRatedGood_Accomplished'),
                        total_TechnicalAdvice = Sum('TechnicalAdvice_Accomplished'),
                        total_AccomplishmentReportDeligatedAssignment = Sum('AccomplishmentReportDeligatedAssignment_Accomplished'),
                        total_FlagRaisingAttendance = Sum('FlagRaisingAttendance_Accomplished'),
                        total_FlagLoweringAttendance = Sum('FlagLoweringAttendance_Accomplished'),
                        total_WellnessProgramAttendance = Sum('WellnessProgramAttendance_Accomplished'),
                        total_SchoolCelebrationAttendance = Sum('SchoolCelebrationAttendance_Accomplished'),
                        total_TrainingAttendance = Sum('TrainingAttendance_Accomplished'),
                        total_FacultyMeetingAttendance = Sum('FacultyMeetingAttendance_Accomplished'),
                        total_AccreditationAttendance = Sum('AccreditationAttendance_Accomplished'),
                        total_SpiritualActivityAttendance = Sum('SpiritualActivityAttendance_Accomplished')
                    )
                    
                elif current_date >= secondmidsem_date and current_date <= secondfinalsem_date:
                    Secondmidterm_instance = IPMT_Form_model.objects.filter(author = request.user, IPCR_Saved__range=(secondmidsem_date, secondfinalsem_date))
                    total_IPCR = Secondmidterm_instance.aggregate(
                        total_syllabus = Sum('syllabus_Accomplished'),
                        total_courseguide = Sum('CourseGuide_Accomplished'),
                        total_SLM = Sum('SLM_Accomplished'),
                        total_SubjectAreas = Sum('SubjectAreas_Accomplished'),
                        total_AttendanceSheet = Sum('AttendanceSheet_Accomplished'),
                        total_ClassRecord = Sum('ClassRecord_Accomplished'),
                        total_TeachingEffectiveness = Sum('TeachingEffectiveness_Accomplished'),
                        total_ClassroomObservation = Sum('ClassroomObservation_Accomplished'),
                        total_TOSRubrics = Sum('TOSRubrics_Accomplished'),
                        total_TestQuestions = Sum('TestQuestions_Accomplished'),
                        total_AnswerKey = Sum('AnswerKey_Accomplished'),
                        total_GradingSheet = Sum('GradingSheet_Accomplished'),
                        total_StudentAdviced = Sum('StudentAdviced_Accomplished'),
                        total_AccomplishmentReport = Sum('AccomplishmentReport_Accomplished'),
                        total_ResearchProposalSubmitted = Sum('ResearchProposalSubmitted_Accomplished'),
                        total_ResearchImplemented = Sum('ResearchImplemented_Accomplished'),
                        total_ResearchPresented = Sum('ResearchPresented_Accomplished'),
                        total_ResearchPublished = Sum('ResearchPublished_Accomplished'),
                        total_ApprovedIPRights = Sum('ApprovedIPRights_Accomplished'),
                        total_ResearchUtilized = Sum('ResearchUtilized_Accomplished'),
                        total_NumberOfCitations = Sum('NumberOfCitations_Accomplished'),
                        total_ExtensionProposalSubmitted = Sum('ExtensionProposalSubmitted_Accomplished'),
                        total_PersonTrained = Sum('PersonTrained_Accomplished'),
                        total_PersonAvailedRatedGood = Sum('PersonAvailedRatedGood_Accomplished'),
                        total_PersonTrainedRatedGood = Sum('PersonTrainedRatedGood_Accomplished'),
                        total_TechnicalAdvice = Sum('TechnicalAdvice_Accomplished'),
                        total_AccomplishmentReportDeligatedAssignment = Sum('AccomplishmentReportDeligatedAssignment_Accomplished'),
                        total_FlagRaisingAttendance = Sum('FlagRaisingAttendance_Accomplished'),
                        total_FlagLoweringAttendance = Sum('FlagLoweringAttendance_Accomplished'),
                        total_WellnessProgramAttendance = Sum('WellnessProgramAttendance_Accomplished'),
                        total_SchoolCelebrationAttendance = Sum('SchoolCelebrationAttendance_Accomplished'),
                        total_TrainingAttendance = Sum('TrainingAttendance_Accomplished'),
                        total_FacultyMeetingAttendance = Sum('FacultyMeetingAttendance_Accomplished'),
                        total_AccreditationAttendance = Sum('AccreditationAttendance_Accomplished'),
                        total_SpiritualActivityAttendance = Sum('SpiritualActivityAttendance_Accomplished')
                    )
                    
                elif current_date >= secondfinalsem_date and current_date <= secondsem_enddate:
                    Secondfinalterm_instance = IPMT_Form_model.objects.filter(author = request.user, IPCR_Saved__range=(secondfinalsem_date, secondsem_enddate))
                    total_IPCR = Secondfinalterm_instance.aggregate(
                        total_syllabus = Sum('syllabus_Accomplished'),
                        total_courseguide = Sum('CourseGuide_Accomplished'),
                        total_SLM = Sum('SLM_Accomplished'),
                        total_SubjectAreas = Sum('SubjectAreas_Accomplished'),
                        total_AttendanceSheet = Sum('AttendanceSheet_Accomplished'),
                        total_ClassRecord = Sum('ClassRecord_Accomplished'),
                        total_TeachingEffectiveness = Sum('TeachingEffectiveness_Accomplished'),
                        total_ClassroomObservation = Sum('ClassroomObservation_Accomplished'),
                        total_TOSRubrics = Sum('TOSRubrics_Accomplished'),
                        total_TestQuestions = Sum('TestQuestions_Accomplished'),
                        total_AnswerKey = Sum('AnswerKey_Accomplished'),
                        total_GradingSheet = Sum('GradingSheet_Accomplished'),
                        total_StudentAdviced = Sum('StudentAdviced_Accomplished'),
                        total_AccomplishmentReport = Sum('AccomplishmentReport_Accomplished'),
                        total_ResearchProposalSubmitted = Sum('ResearchProposalSubmitted_Accomplished'),
                        total_ResearchImplemented = Sum('ResearchImplemented_Accomplished'),
                        total_ResearchPresented = Sum('ResearchPresented_Accomplished'),
                        total_ResearchPublished = Sum('ResearchPublished_Accomplished'),
                        total_ApprovedIPRights = Sum('ApprovedIPRights_Accomplished'),
                        total_ResearchUtilized = Sum('ResearchUtilized_Accomplished'),
                        total_NumberOfCitations = Sum('NumberOfCitations_Accomplished'),
                        total_ExtensionProposalSubmitted = Sum('ExtensionProposalSubmitted_Accomplished'),
                        total_PersonTrained = Sum('PersonTrained_Accomplished'),
                        total_PersonAvailedRatedGood = Sum('PersonAvailedRatedGood_Accomplished'),
                        total_PersonTrainedRatedGood = Sum('PersonTrainedRatedGood_Accomplished'),
                        total_TechnicalAdvice = Sum('TechnicalAdvice_Accomplished'),
                        total_AccomplishmentReportDeligatedAssignment = Sum('AccomplishmentReportDeligatedAssignment_Accomplished'),
                        total_FlagRaisingAttendance = Sum('FlagRaisingAttendance_Accomplished'),
                        total_FlagLoweringAttendance = Sum('FlagLoweringAttendance_Accomplished'),
                        total_WellnessProgramAttendance = Sum('WellnessProgramAttendance_Accomplished'),
                        total_SchoolCelebrationAttendance = Sum('SchoolCelebrationAttendance_Accomplished'),
                        total_TrainingAttendance = Sum('TrainingAttendance_Accomplished'),
                        total_FacultyMeetingAttendance = Sum('FacultyMeetingAttendance_Accomplished'),
                        total_AccreditationAttendance = Sum('AccreditationAttendance_Accomplished'),
                        total_SpiritualActivityAttendance = Sum('SpiritualActivityAttendance_Accomplished')
                    )    
                
                #Obtaining the new accomplished data for a new IPMT model instance
                source_instance = IPCR_Form_model.objects.filter(author=request.user).order_by('-id').last()
                destination_instance = IPMT_Form_model.objects.create(author = request.user) 
                
                destination_instance.syllabus_Accomplished = source_instance.syllabus_Accomplished - total_IPCR.get('total_syllabus')
                destination_instance.CourseGuide_Accomplished = source_instance.CourseGuide_Accomplished - total_IPCR.get('total_courseguide')
                destination_instance.SLM_Accomplished = source_instance.SLM_Accomplished - total_IPCR.get('total_SLM')
                destination_instance.SubjectAreas_Accomplished = source_instance.SubjectAreas_Accomplished - total_IPCR.get('total_SubjectAreas')
                destination_instance.AttendanceSheet_Accomplished = source_instance.AttendanceSheet_Accomplished - total_IPCR.get('total_AttendanceSheet')
                destination_instance.ClassRecord_Accomplished = source_instance.ClassRecord_Accomplished - total_IPCR.get('total_ClassRecord')
                destination_instance.TeachingEffectiveness_Accomplished = source_instance.TeachingEffectiveness_Accomplished - total_IPCR.get('total_TeachingEffectiveness')
                destination_instance.ClassroomObservation_Accomplished = source_instance.ClassroomObservation_Accomplished - total_IPCR.get('total_ClassroomObservation')
                destination_instance.TOSRubrics_Accomplished = source_instance.MidtermTOSRubrics_Accomplished + source_instance.FinaltermTOSRubrics_Accomplished - total_IPCR.get('total_TOSRubrics')
                destination_instance.TestQuestions_Accomplished = source_instance.MidtermTestQuestions_Accomplished + source_instance.FinaltermTestQuestions_Accomplished - total_IPCR.get('total_TestQuestions')
                destination_instance.AnswerKey_Accomplished = source_instance.MidtermAnswerKey_Accomplished + source_instance.FinaltermAnswerKey_Accomplished - total_IPCR.get('total_AnswerKey')
                destination_instance.GradingSheet_Accomplished = source_instance.GradingSheet_Accomplished - total_IPCR.get('total_GradingSheet')
                destination_instance.StudentAdviced_Accomplished = source_instance.StudentAdviced_Accomplished - total_IPCR.get('total_StudentAdviced')
                destination_instance.AccomplishmentReport_Accomplished = source_instance.AccomplishmentReport_Accomplished - total_IPCR.get('total_AccomplishmentReport')
                destination_instance.ResearchProposalSubmitted_Accomplished = source_instance.ResearchProposalSubmitted_Accomplished- total_IPCR.get('total_ResearchProposalSubmitted')
                destination_instance.ResearchImplemented_Accomplished = source_instance.ResearchImplemented_Accomplished - total_IPCR.get('total_ResearchImplemented')
                destination_instance.ResearchPresented_Accomplished = source_instance.ResearchPresented_Accomplished - total_IPCR.get('total_ResearchPresented')
                destination_instance.ResearchPublished_Accomplished = source_instance.ResearchPublished_Accomplished - total_IPCR.get('total_ResearchPublished')
                destination_instance.ApprovedIPRights_Accomplished = source_instance.ApprovedIPRights_Accomplished - total_IPCR.get('total_ApprovedIPRights')
                destination_instance.ResearchUtilized_Accomplished = source_instance.ResearchUtilized_Accomplished - total_IPCR.get('total_ResearchUtilized')
                destination_instance.NumberOfCitations_Accomplished = source_instance.NumberOfCitations_Accomplished - total_IPCR.get('total_NumberOfCitations')
                destination_instance.ExtensionProposalSubmitted_Accomplished = source_instance.ExtensionProposalSubmitted_Accomplished - total_IPCR.get('total_ExtensionProposalSubmitted')
                destination_instance.PersonTrained_Accomplished = source_instance.PersonTrained_Accomplished - total_IPCR.get('total_PersonTrained')
                destination_instance.PersonAvailedRatedGood_Accomplished = source_instance.PersonAvailedRatedGood_Accomplished - total_IPCR.get('total_PersonAvailedRatedGood')           
                destination_instance.PersonTrainedRatedGood_Accomplished = source_instance.PersonTrainedRatedGood_Accomplished - total_IPCR.get('total_PersonTrainedRatedGood')
                destination_instance.TechnicalAdvice_Accomplished = source_instance.TechnicalAdvice_Accomplished - total_IPCR.get('total_TechnicalAdvice')
                destination_instance.AccomplishmentReportDeligatedAssignment_Accomplished = source_instance.AccomplishmentReportDeligatedAssignment_Accomplished - total_IPCR.get('total_AccomplishmentReportDeligatedAssignment')
                destination_instance.FlagRaisingAttendance_Accomplished = source_instance.FlagRaisingAttendance_Accomplished - total_IPCR.get('total_FlagRaisingAttendance')
                destination_instance.FlagLoweringAttendance_Accomplished = source_instance.FlagLoweringAttendance_Accomplished - total_IPCR.get('total_FlagLoweringAttendance')
                destination_instance.WellnessProgramAttendance_Accomplished = source_instance.WellnessProgramAttendance_Accomplished - total_IPCR.get('total_WellnessProgramAttendance')
                destination_instance.SchoolCelebrationAttendance_Accomplished = source_instance.SchoolCelebrationAttendance_Accomplished - total_IPCR.get('total_SchoolCelebrationAttendance')
                destination_instance.TrainingAttendance_Accomplished = source_instance.TrainingAttendance_Accomplished - total_IPCR.get('total_TrainingAttendance')
                destination_instance.FacultyMeetingAttendance_Accomplished = source_instance.FacultyMeetingAttendance_Accomplished - total_IPCR.get('total_FacultyMeetingAttendance')
                destination_instance.AccreditationAttendance_Accomplished = source_instance.AccreditationAttendance_Accomplished - total_IPCR.get('total_AccreditationAttendance')
                destination_instance.SpiritualActivityAttendance_Accomplished = source_instance.SpiritualActivityAttendance_Accomplished - total_IPCR.get('total_AccreditationAttendance')
                destination_instance.IPCR_Saved = date.today()
                
                destination_instance.save()
            
            model_instance.save()
            messages.success(request, "You've successfully saved your IPCR form.")
            return redirect('IPCR_Form')

    else:
        forms = IPCRForm(instance=existing_instance)

    context = {
        'forms': forms,
        'current_user' : current_user,
    }
    return render(request, 'forms/IPCRForm_Submit.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])
def IPCR_Form_Submit(request):
    #This handles the submission of the user's IPCR form
    check_instance = IPCR_Form_model_submitted.objects.filter(author=request.user).order_by('-IPCR_Submitted').first()
    current_date = datetime.now().date()
    current_year = datetime.now().year
    firstmidsem_month = 8
    firstfinalsem_month = 10
    firstsem_endmonth = 1
    firstsem_day = 25
    secondmidsem_month = 2
    secondfinalsem_month = 4
    secondsem_endmonth = 6
    secondsem_day = 5
    
    firstmidsem_date = datetime(current_year, firstmidsem_month, firstsem_day).date()
    firstfinalsem_date = datetime(current_year, firstfinalsem_month, firstsem_day).date()
    firstsem_enddate = datetime(current_year, firstsem_endmonth, firstsem_day).date()
    
    secondmidsem_date = datetime(current_year, secondmidsem_month, secondsem_day).date()
    secondfinalsem_date = datetime(current_year, secondfinalsem_month, secondsem_day).date()
    secondsem_enddate = datetime(current_year, secondsem_endmonth, secondsem_day).date()
    
    if (request.method == "POST"):
        
        if IPCR_Form_model_submitted.objects.filter(author=request.user).exists():
            if current_date >= firstmidsem_date and current_date <= firstfinalsem_date:
                if check_instance.IPCR_Submitted >= firstmidsem_date and check_instance.IPCR_Submitted <= firstfinalsem_date:
                    return redirect('IPCR_Form_Already_Submitted')
                
                else:
                    IPCR_Form_Submit_snip(request)
                
            elif current_date >= firstfinalsem_date and current_date <= firstsem_enddate:
                if check_instance.IPCR_Submitted >= firstfinalsem_date and check_instance.IPCR_Submitted <= firstsem_enddate:
                    return redirect('IPCR_Form_Already_Submitted')
                
                else:
                    IPCR_Form_Submit_snip(request)

            elif current_date >= secondmidsem_date and current_date <= secondfinalsem_date:
                if check_instance.IPCR_Submitted >= secondmidsem_date and check_instance.IPCR_Submitted <= secondfinalsem_date:
                    return redirect('IPCR_Form_Already_Submitted')
                
                else:
                    IPCR_Form_Submit_snip(request)

            elif current_date >= secondfinalsem_date and current_date <= secondsem_enddate:
                if check_instance.IPCR_Submitted >= secondfinalsem_date and check_instance.IPCR_Submitted <= secondsem_enddate:
                    return redirect('IPCR_Form_Already_Submitted')
                
                else:
                    IPCR_Form_Submit_snip(request)
        else:
            IPCR_Form_Submit_snip(request)
    
    return render(request, 'forms/IPCRForm_SubmitNow.html')

def IPCR_Form_Submit_snip(request):
    #The function for handling the submission of the user
    user = request.user
    first_name = user.first_name
    last_name = user.last_name
    
    grade_instance = IPCR_Rating.objects.create(author = user)
    
    grade_instance.syllabus_QTY = random.randint(1, 10)
    grade_instance.syllabus_QLE = random.randint(1, 10)
    grade_instance.syllabus_T = random.randint(1, 10)
    grade_instance.syllabus_A = (grade_instance.syllabus_QTY + grade_instance.syllabus_QLE + grade_instance.syllabus_T)/3
    
    grade_instance.CourseGuide_QTY = random.randint(1, 10)
    grade_instance.CourseGuide_QLE = random.randint(1, 10)
    grade_instance.CourseGuide_T = random.randint(1, 10)
    grade_instance.CourseGuide_A = (grade_instance.CourseGuide_QTY + grade_instance.CourseGuide_QLE + grade_instance.CourseGuide_T)/3
    
    grade_instance.SLM_QTY = random.randint(1, 10)
    grade_instance.SLM_QLE = random.randint(1, 10)
    grade_instance.SLM_T = random.randint(1, 10)
    grade_instance.SLM_A = (grade_instance.SLM_QTY + grade_instance.SLM_QLE + grade_instance.SLM_T)/3
    
    grade_instance.SubjectAreas_QTY = random.randint(1, 10)
    grade_instance.SubjectAreas_QLE = random.randint(1, 10)
    grade_instance.SubjectAreas_T = random.randint(1, 10)
    grade_instance.SubjectAreas_A = (grade_instance.SubjectAreas_QTY + grade_instance.SubjectAreas_QLE + grade_instance.SubjectAreas_T)/3
    
    grade_instance.AttendanceSheet_QTY = random.randint(1, 10)
    grade_instance.AttendanceSheet_QLE = random.randint(1, 10)
    grade_instance.AttendanceSheet_T = random.randint(1, 10)
    grade_instance.AttendanceSheet_A = (grade_instance.AttendanceSheet_QTY + grade_instance.AttendanceSheet_QLE + grade_instance.AttendanceSheet_T)/3
    
    grade_instance.ClassRecord_QTY = random.randint(1, 10)
    grade_instance.ClassRecord_QLE = random.randint(1, 10)
    grade_instance.ClassRecord_T = random.randint(1, 10)
    grade_instance.ClassRecord_A = (grade_instance.ClassRecord_QTY + grade_instance.ClassRecord_QLE + grade_instance.ClassRecord_T)/3
    
    grade_instance.TeachingEffectiveness_QTY = random.randint(1, 10)
    grade_instance.TeachingEffectiveness_QLE = random.randint(1, 10)
    grade_instance.TeachingEffectiveness_T = random.randint(1, 10)
    grade_instance.TeachingEffectiveness_A = (grade_instance.TeachingEffectiveness_QTY + grade_instance.TeachingEffectiveness_QLE + grade_instance.TeachingEffectiveness_T)/3
    
    grade_instance.ClassroomObservation_QTY = random.randint(1, 10)
    grade_instance.ClassroomObservation_QLE = random.randint(1, 10)
    grade_instance.ClassroomObservation_T = random.randint(1, 10)
    grade_instance.ClassroomObservation_A = (grade_instance.ClassroomObservation_QTY + grade_instance.ClassroomObservation_QLE + grade_instance.ClassroomObservation_T)/3
    
    grade_instance.MidtermTOSRubrics_QTY = random.randint(1, 10)
    grade_instance.MidtermTOSRubrics_QLE = random.randint(1, 10)
    grade_instance.MidtermTOSRubrics_T = random.randint(1, 10)
    grade_instance.MidtermTOSRubrics_A = (grade_instance.MidtermTOSRubrics_QTY + grade_instance.MidtermTOSRubrics_QLE + grade_instance.MidtermTOSRubrics_T)/3
    
    grade_instance.FinaltermTOSRubrics_QTY = random.randint(1, 10)
    grade_instance.FinaltermTOSRubrics_QLE = random.randint(1, 10)
    grade_instance.FinaltermTOSRubrics_T = random.randint(1, 10)
    grade_instance.FinaltermTOSRubrics_A = (grade_instance.FinaltermTOSRubrics_QTY + grade_instance.FinaltermTOSRubrics_QLE + grade_instance.FinaltermTOSRubrics_T)/3
    
    grade_instance.MidtermTestQuestions_QTY = random.randint(1, 10)
    grade_instance.MidtermTestQuestions_QLE = random.randint(1, 10)
    grade_instance.MidtermTestQuestions_T = random.randint(1, 10)
    grade_instance.MidtermTestQuestions_A = (grade_instance.MidtermTestQuestions_QTY + grade_instance.MidtermTestQuestions_QLE + grade_instance.MidtermTestQuestions_T)/3
    
    grade_instance.FinaltermTestQuestions_QTY = random.randint(1, 10)
    grade_instance.FinaltermTestQuestions_QLE = random.randint(1, 10)
    grade_instance.FinaltermTestQuestions_T = random.randint(1, 10)
    grade_instance.FinaltermTestQuestions_A = (grade_instance.FinaltermTestQuestions_QTY + grade_instance.FinaltermTestQuestions_QLE + grade_instance.FinaltermTestQuestions_T)/3
    
    grade_instance.MidtermAnswerKey_QTY = random.randint(1, 10)
    grade_instance.MidtermAnswerKey_QLE = random.randint(1, 10)
    grade_instance.MidtermAnswerKey_T = random.randint(1, 10)
    grade_instance.MidtermAnswerKey_A = (grade_instance.MidtermAnswerKey_QTY + grade_instance.MidtermAnswerKey_QLE + grade_instance.MidtermAnswerKey_T)/3
    
    grade_instance.FinaltermAnswerKey_QTY = random.randint(1, 10)
    grade_instance.FinaltermAnswerKey_QLE = random.randint(1, 10)
    grade_instance.FinaltermAnswerKey_T = random.randint(1, 10)
    grade_instance.FinaltermAnswerKey_A = (grade_instance.FinaltermAnswerKey_QTY + grade_instance.FinaltermAnswerKey_QLE + grade_instance.FinaltermAnswerKey_T)/3
    
    grade_instance.GradingSheet_QTY = random.randint(1, 10)
    grade_instance.GradingSheet_QLE = random.randint(1, 10)
    grade_instance.GradingSheet_T = random.randint(1, 10)
    grade_instance.GradingSheet_A = (grade_instance.GradingSheet_QTY + grade_instance.GradingSheet_QLE + grade_instance.GradingSheet_T)/3
    
    grade_instance.StudentAdviced_QTY = random.randint(1, 10)
    grade_instance.StudentAdviced_QLE = random.randint(1, 10)
    grade_instance.StudentAdviced_T = random.randint(1, 10)
    grade_instance.StudentAdviced_A = (grade_instance.StudentAdviced_QTY + grade_instance.StudentAdviced_QLE + grade_instance.StudentAdviced_T)/3
    
    grade_instance.AccomplishmentReport_QTY = random.randint(1, 10)
    grade_instance.AccomplishmentReport_QLE = random.randint(1, 10)
    grade_instance.AccomplishmentReport_T = random.randint(1, 10)
    grade_instance.AccomplishmentReport_A = (grade_instance.AccomplishmentReport_QTY + grade_instance.AccomplishmentReport_QLE + grade_instance.AccomplishmentReport_T)/3
    
    grade_instance.ResearchProposalSubmitted_QTY = random.randint(1, 10)
    grade_instance.ResearchProposalSubmitted_QLE = random.randint(1, 10)
    grade_instance.ResearchProposalSubmitted_T = random.randint(1, 10)
    grade_instance.ResearchProposalSubmitted_A = (grade_instance.ResearchProposalSubmitted_QTY + grade_instance.ResearchProposalSubmitted_QLE + grade_instance.ResearchProposalSubmitted_T)/3
    
    grade_instance.ResearchImplemented_QTY = random.randint(1, 10)
    grade_instance.ResearchImplemented_QLE = random.randint(1, 10)
    grade_instance.ResearchImplemented_T = random.randint(1, 10)
    grade_instance.ResearchImplemented_A = (grade_instance.ResearchImplemented_QTY + grade_instance.ResearchImplemented_QLE + grade_instance.ResearchImplemented_T)/3
    
    grade_instance.ResearchPresented_QTY = random.randint(1, 10)
    grade_instance.ResearchPresented_QLE = random.randint(1, 10)
    grade_instance.ResearchPresented_T = random.randint(1, 10)
    grade_instance.ResearchPresented_A = (grade_instance.ResearchPresented_QTY + grade_instance.ResearchPresented_QLE + grade_instance.ResearchPresented_T)/3
    
    grade_instance.ResearchPublished_QTY = random.randint(1, 10)
    grade_instance.ResearchPublished_QLE = random.randint(1, 10)
    grade_instance.ResearchPublished_T = random.randint(1, 10)
    grade_instance.ResearchPublished_A = (grade_instance.ResearchPublished_QTY + grade_instance.ResearchPublished_QLE + grade_instance.ResearchPublished_T)/3
    
    grade_instance.ApprovedIPRights_QTY = random.randint(1, 10)
    grade_instance.ApprovedIPRights_QLE = random.randint(1, 10)
    grade_instance.ApprovedIPRights_T = random.randint(1, 10)
    grade_instance.ApprovedIPRights_A = (grade_instance.ApprovedIPRights_QTY + grade_instance.ApprovedIPRights_QLE + grade_instance.ApprovedIPRights_T)/3
    
    grade_instance.ResearchUtilized_QTY = random.randint(1, 10)
    grade_instance.ResearchUtilized_QLE = random.randint(1, 10)
    grade_instance.ResearchUtilized_T = random.randint(1, 10)
    grade_instance.ResearchUtilized_A = (grade_instance.ResearchUtilized_QTY + grade_instance.ResearchUtilized_QLE + grade_instance.ResearchUtilized_T)/3
    
    grade_instance.NumberOfCitations_QTY = random.randint(1, 10)
    grade_instance.NumberOfCitations_QLE = random.randint(1, 10)
    grade_instance.NumberOfCitations_T = random.randint(1, 10)
    grade_instance.NumberOfCitations_A = (grade_instance.NumberOfCitations_QTY + grade_instance.NumberOfCitations_QLE + grade_instance.NumberOfCitations_T)/3
    
    grade_instance.ExtensionProposalSubmitted_QTY = random.randint(1, 10)
    grade_instance.ExtensionProposalSubmitted_QLE = random.randint(1, 10)
    grade_instance.ExtensionProposalSubmitted_T = random.randint(1, 10)
    grade_instance.ExtensionProposalSubmitted_A = (grade_instance.ExtensionProposalSubmitted_QTY + grade_instance.ExtensionProposalSubmitted_QLE + grade_instance.ExtensionProposalSubmitted_T)/3
    
    grade_instance.PersonTrained_QTY = random.randint(1, 10)
    grade_instance.PersonTrained_QLE = random.randint(1, 10)
    grade_instance.PersonTrained_T = random.randint(1, 10)
    grade_instance.PersonTrained_A = (grade_instance.PersonTrained_QTY + grade_instance.PersonTrained_QLE + grade_instance.PersonTrained_T)/3
    
    grade_instance.PersonAvailedRatedGood_QTY = random.randint(1, 10)
    grade_instance.PersonAvailedRatedGood_QLE = random.randint(1, 10)
    grade_instance.PersonAvailedRatedGood_T = random.randint(1, 10)
    grade_instance.PersonAvailedRatedGood_A = (grade_instance.PersonAvailedRatedGood_QTY + grade_instance.PersonAvailedRatedGood_QLE + grade_instance.PersonAvailedRatedGood_T)/3
    
    grade_instance.PersonTrainedRatedGood_QTY = random.randint(1, 10)
    grade_instance.PersonTrainedRatedGood_QLE = random.randint(1, 10)
    grade_instance.PersonTrainedRatedGood_T = random.randint(1, 10)
    grade_instance.PersonTrainedRatedGood_A = (grade_instance.PersonTrainedRatedGood_QTY + grade_instance.PersonTrainedRatedGood_QLE + grade_instance.PersonTrainedRatedGood_T)/3
    
    grade_instance.TechnicalAdvice_QTY = random.randint(1, 10)
    grade_instance.TechnicalAdvice_QLE = random.randint(1, 10)
    grade_instance.TechnicalAdvice_T = random.randint(1, 10)
    grade_instance.TechnicalAdvice_A = (grade_instance.TechnicalAdvice_QTY + grade_instance.TechnicalAdvice_QLE + grade_instance.TechnicalAdvice_T)/3
    
    grade_instance.AccomplishmentReportDeligatedAssignment_QTY = random.randint(1, 10)
    grade_instance.AccomplishmentReportDeligatedAssignment_QLE = random.randint(1, 10)
    grade_instance.AccomplishmentReportDeligatedAssignment_T = random.randint(1, 10)
    grade_instance.AccomplishmentReportDeligatedAssignment_A = (grade_instance.AccomplishmentReportDeligatedAssignment_QTY + grade_instance.AccomplishmentReportDeligatedAssignment_QLE + grade_instance.AccomplishmentReportDeligatedAssignment_T)/3
    
    grade_instance.FlagRaisingAttendance_QTY = random.randint(1, 10)
    grade_instance.FlagRaisingAttendance_QLE = random.randint(1, 10)
    grade_instance.FlagRaisingAttendance_T = random.randint(1, 10)
    grade_instance.FlagRaisingAttendance_A = (grade_instance.FlagRaisingAttendance_QTY + grade_instance.FlagRaisingAttendance_QLE + grade_instance.FlagRaisingAttendance_T)/3
    
    grade_instance.FlagLoweringAttendance_QTY = random.randint(1, 10)
    grade_instance.FlagLoweringAttendance_QLE = random.randint(1, 10)
    grade_instance.FlagLoweringAttendance_T = random.randint(1, 10)
    grade_instance.FlagLoweringAttendance_A = (grade_instance.FlagLoweringAttendance_QTY + grade_instance.FlagLoweringAttendance_QLE + grade_instance.FlagLoweringAttendance_T)/3
    
    grade_instance.WellnessProgramAttendance_QTY = random.randint(1, 10)
    grade_instance.WellnessProgramAttendance_QLE = random.randint(1, 10)
    grade_instance.WellnessProgramAttendance_T = random.randint(1, 10)
    grade_instance.WellnessProgramAttendance_A = (grade_instance.WellnessProgramAttendance_QTY + grade_instance.WellnessProgramAttendance_QLE + grade_instance.WellnessProgramAttendance_T)/3
    
    grade_instance.SchoolCelebrationAttendance_QTY = random.randint(1, 10)
    grade_instance.SchoolCelebrationAttendance_QLE = random.randint(1, 10)
    grade_instance.SchoolCelebrationAttendance_T = random.randint(1, 10)
    grade_instance.SchoolCelebrationAttendance_A = (grade_instance.SchoolCelebrationAttendance_QTY + grade_instance.SchoolCelebrationAttendance_QLE + grade_instance.SchoolCelebrationAttendance_T)/3
    
    grade_instance.TrainingAttendance_QTY = random.randint(1, 10)
    grade_instance.TrainingAttendance_QLE = random.randint(1, 10)
    grade_instance.TrainingAttendance_T = random.randint(1, 10)
    grade_instance.TrainingAttendance_A = (grade_instance.TrainingAttendance_QTY + grade_instance.TrainingAttendance_QLE + grade_instance.TrainingAttendance_T)/3
    
    grade_instance.FacultyMeetingAttendance_QTY = random.randint(1, 10)
    grade_instance.FacultyMeetingAttendance_QLE = random.randint(1, 10)
    grade_instance.FacultyMeetingAttendance_T = random.randint(1, 10)
    grade_instance.FacultyMeetingAttendance_A = (grade_instance.FacultyMeetingAttendance_QTY + grade_instance.FacultyMeetingAttendance_QLE + grade_instance.FacultyMeetingAttendance_T)/3
    
    grade_instance.AccreditationAttendance_QTY = random.randint(1, 10)
    grade_instance.AccreditationAttendance_QLE = random.randint(1, 10)
    grade_instance.AccreditationAttendance_T = random.randint(1, 10)
    grade_instance.AccreditationAttendance_A = (grade_instance.AccreditationAttendance_QTY + grade_instance.AccreditationAttendance_QLE + grade_instance.AccreditationAttendance_T)/3
    
    grade_instance.SpiritualActivityAttendance_QTY = random.randint(1, 10)
    grade_instance.SpiritualActivityAttendance_QLE = random.randint(1, 10)
    grade_instance.SpiritualActivityAttendance_T = random.randint(1, 10)
    grade_instance.SpiritualActivityAttendance_A = (grade_instance.SpiritualActivityAttendance_QTY + grade_instance.SpiritualActivityAttendance_QLE + grade_instance.SpiritualActivityAttendance_T)/3
    
    grade_instance.IPCR_Submitted = datetime.now().date()
    grade_instance.save()
        
    new_instance = IPCR_Form_model_submitted.objects.create(author = user, user_fullname = f"{first_name} {last_name}")
    source_instance = IPCR_Form_model.objects.filter(author=request.user).order_by('-id').first()
    
    new_instance.syllabus_Target = source_instance.syllabus_Target
    new_instance.syllabus_Accomplished = source_instance.syllabus_Accomplished
    new_instance.CourseGuide_Target = source_instance.CourseGuide_Target
    new_instance.CourseGuide_Accomplished = source_instance.CourseGuide_Accomplished
    new_instance.SLM_Target = source_instance.SLM_Target
    new_instance.SLM_Accomplished = source_instance.SLM_Accomplished
    new_instance.SubjectAreas_Target = source_instance.SubjectAreas_Target
    new_instance.SubjectAreas_Accomplished = source_instance.SubjectAreas_Accomplished
    new_instance.AttendanceSheet_Target = source_instance.AttendanceSheet_Target
    new_instance.AttendanceSheet_Accomplished = source_instance.AttendanceSheet_Accomplished
    new_instance.ClassRecord_Target = source_instance.ClassRecord_Target
    new_instance.ClassRecord_Accomplished = source_instance.ClassRecord_Accomplished
    new_instance.TeachingEffectiveness_Target = source_instance.TeachingEffectiveness_Target
    new_instance.TeachingEffectiveness_Accomplished = source_instance.TeachingEffectiveness_Accomplished
    new_instance.ClassroomObservation_Target = source_instance.ClassroomObservation_Target
    new_instance.ClassroomObservation_Accomplished = source_instance.ClassroomObservation_Accomplished
    new_instance.MidtermTOSRubrics_Target = source_instance.MidtermTOSRubrics_Target
    new_instance.MidtermTOSRubrics_Accomplished = source_instance.MidtermTOSRubrics_Accomplished
    new_instance.FinaltermTOSRubrics_Target = source_instance.FinaltermTOSRubrics_Target
    new_instance.FinaltermTOSRubrics_Accomplished = source_instance.FinaltermTOSRubrics_Accomplished
    new_instance.MidtermTestQuestions_Target = source_instance.MidtermTestQuestions_Target
    new_instance.MidtermTestQuestions_Accomplished = source_instance.MidtermTestQuestions_Accomplished
    new_instance.FinaltermTestQuestions_Target = source_instance.FinaltermTestQuestions_Target
    new_instance.FinaltermTestQuestions_Accomplished = source_instance.FinaltermTestQuestions_Accomplished
    new_instance.MidtermAnswerKey_Target = source_instance.MidtermAnswerKey_Target
    new_instance.MidtermAnswerKey_Accomplished = source_instance.MidtermAnswerKey_Accomplished
    new_instance.FinaltermAnswerKey_Target = source_instance.FinaltermAnswerKey_Target
    new_instance.FinaltermAnswerKey_Accomplished = source_instance.FinaltermAnswerKey_Accomplished
    new_instance.GradingSheet_Target = source_instance.GradingSheet_Target
    new_instance.GradingSheet_Accomplished = source_instance.GradingSheet_Accomplished
    new_instance.StudentAdviced_Target = source_instance.StudentAdviced_Target
    new_instance.StudentAdviced_Accomplished = source_instance.StudentAdviced_Accomplished
    new_instance.AccomplishmentReport_Target = source_instance.AccomplishmentReport_Target
    new_instance.AccomplishmentReport_Accomplished = source_instance.AccomplishmentReport_Accomplished
    new_instance.ResearchProposalSubmitted_Target = source_instance.ResearchProposalSubmitted_Target
    new_instance.ResearchProposalSubmitted_Accomplished = source_instance.ResearchProposalSubmitted_Accomplished
    new_instance.ResearchImplemented_Target = source_instance.ResearchImplemented_Target
    new_instance.ResearchImplemented_Accomplished = source_instance.ResearchImplemented_Accomplished
    new_instance.ResearchPresented_Target = source_instance.ResearchPresented_Target
    new_instance.ResearchPresented_Accomplished = source_instance.ResearchPresented_Accomplished
    new_instance.ResearchPublished_Target = source_instance.ResearchPublished_Target
    new_instance.ResearchPublished_Accomplished = source_instance.ResearchPublished_Accomplished
    new_instance.ApprovedIPRights_Target = source_instance.ApprovedIPRights_Target
    new_instance.ApprovedIPRights_Accomplished = source_instance.ApprovedIPRights_Accomplished
    new_instance.ResearchUtilized_Target = source_instance.ResearchUtilized_Target
    new_instance.ResearchUtilized_Accomplished = source_instance.ResearchUtilized_Accomplished
    new_instance.NumberOfCitations_Target = source_instance.NumberOfCitations_Target
    new_instance.NumberOfCitations_Accomplished = source_instance.NumberOfCitations_Accomplished
    new_instance.ExtensionProposalSubmitted_Target = source_instance.ExtensionProposalSubmitted_Target
    new_instance.ExtensionProposalSubmitted_Accomplished = source_instance.ExtensionProposalSubmitted_Accomplished
    new_instance.PersonTrained_Target = source_instance.PersonTrained_Target
    new_instance.PersonTrained_Accomplished = source_instance.PersonTrained_Accomplished
    new_instance.PersonAvailedRatedGood_Target = source_instance.PersonAvailedRatedGood_Target
    new_instance.PersonAvailedRatedGood_Accomplished = source_instance.PersonAvailedRatedGood_Accomplished
    new_instance.PersonTrainedRatedGood_Target = source_instance.PersonTrainedRatedGood_Target
    new_instance.PersonTrainedRatedGood_Accomplished = source_instance.PersonTrainedRatedGood_Accomplished
    new_instance.TechnicalAdvice_Target = source_instance.TechnicalAdvice_Target
    new_instance.TechnicalAdvice_Accomplished = source_instance.TechnicalAdvice_Accomplished
    new_instance.AccomplishmentReportDeligatedAssignment_Target = source_instance.AccomplishmentReportDeligatedAssignment_Target
    new_instance.AccomplishmentReportDeligatedAssignment_Accomplished = source_instance.AccomplishmentReportDeligatedAssignment_Accomplished
    new_instance.FlagRaisingAttendance_Target = source_instance.FlagRaisingAttendance_Target
    new_instance.FlagRaisingAttendance_Accomplished = source_instance.FlagRaisingAttendance_Accomplished
    new_instance.FlagLoweringAttendance_Target = source_instance.FlagLoweringAttendance_Target
    new_instance.FlagLoweringAttendance_Accomplished = source_instance.FlagLoweringAttendance_Accomplished
    new_instance.WellnessProgramAttendance_Target = source_instance.WellnessProgramAttendance_Target
    new_instance.WellnessProgramAttendance_Accomplished = source_instance.WellnessProgramAttendance_Accomplished
    new_instance.SchoolCelebrationAttendance_Target = source_instance.SchoolCelebrationAttendance_Target
    new_instance.SchoolCelebrationAttendance_Accomplished = source_instance.SchoolCelebrationAttendance_Accomplished
    new_instance.TrainingAttendance_Target = source_instance.TrainingAttendance_Target
    new_instance.TrainingAttendance_Accomplished = source_instance.TrainingAttendance_Accomplished
    new_instance.FacultyMeetingAttendance_Target = source_instance.FacultyMeetingAttendance_Target
    new_instance.FacultyMeetingAttendance_Accomplished = source_instance.FacultyMeetingAttendance_Accomplished
    new_instance.AccreditationAttendance_Target = source_instance.AccreditationAttendance_Target
    new_instance.AccreditationAttendance_Accomplished = source_instance.AccreditationAttendance_Accomplished
    new_instance.SpiritualActivityAttendance_Target = source_instance.SpiritualActivityAttendance_Target
    new_instance.SpiritualActivityAttendance_Accomplished = source_instance.SpiritualActivityAttendance_Accomplished
    new_instance.IPCR_Deadline = source_instance.IPCR_Deadline
    new_instance.IPCR_Submitted = date.today()
    new_instance.department = source_instance.department
    
    current_year = datetime.now().year
    month_jan = 1
    month_feb = 2
    month_mar = 3
    month_apr = 4
    month_may = 5
    month_jun = 6
    month_jul = 7
    month_aug = 8
    month_sep = 9
    month_oct = 10
    month_nov = 11
    month_dec = 12
    current_user = request.user

    Remarks_IPMT = IPMT_Remarks.objects.create(author = user)
    January_IPMT = IPMT_Form_model_submitted_1.objects.create(author = user)
    February_IPMT = IPMT_Form_model_submitted_2.objects.create(author = user)
    March_IPMT = IPMT_Form_model_submitted_3.objects.create(author = user)
    April_IPMT = IPMT_Form_model_submitted_4.objects.create(author = user)
    May_IPMT = IPMT_Form_model_submitted_5.objects.create(author = user)
    June_IPMT = IPMT_Form_model_submitted_6.objects.create(author = user)
    July_IPMT = IPMT_Form_model_submitted_7.objects.create(author = user)
    August_IPMT = IPMT_Form_model_submitted_8.objects.create(author = user)
    September_IPMT = IPMT_Form_model_submitted_9.objects.create(author = user)
    October_IPMT = IPMT_Form_model_submitted_10.objects.create(author = user)
    November_IPMT = IPMT_Form_model_submitted_11.objects.create(author = user)
    December_IPMT = IPMT_Form_model_submitted_12.objects.create(author = user)
    
    January_submissions = IPMT_Form_model.objects.filter(
        Q(author=current_user),
        Q(IPCR_Saved__month=month_jan),
        Q(IPCR_Saved__year=current_year),
    )
    
    January_IPMT.syllabus_Accomplished = January_submissions.aggregate(syllabus_Accomplished=Sum('syllabus_Accomplished'))['syllabus_Accomplished']
    January_IPMT.CourseGuide_Accomplished = January_submissions.aggregate(CourseGuide_Accomplished=Sum('CourseGuide_Accomplished'))['CourseGuide_Accomplished']
    January_IPMT.SLM_Accomplished = January_submissions.aggregate(SLM_Accomplished=Sum('SLM_Accomplished'))['SLM_Accomplished']
    January_IPMT.SubjectAreas_Accomplished = January_submissions.aggregate(SubjectAreas_Accomplished=Sum('SubjectAreas_Accomplished'))['SubjectAreas_Accomplished']
    January_IPMT.AttendanceSheet_Accomplished = January_submissions.aggregate(AttendanceSheet_Accomplished=Sum('AttendanceSheet_Accomplished'))['AttendanceSheet_Accomplished']
    January_IPMT.ClassRecord_Accomplished = January_submissions.aggregate(ClassRecord_Accomplished=Sum('ClassRecord_Accomplished'))['ClassRecord_Accomplished']
    January_IPMT.TeachingEffectiveness_Accomplished = January_submissions.aggregate(TeachingEffectiveness_Accomplished=Sum('TeachingEffectiveness_Accomplished'))['TeachingEffectiveness_Accomplished']
    January_IPMT.ClassroomObservation_Accomplished = January_submissions.aggregate(ClassroomObservation_Accomplished=Sum('ClassroomObservation_Accomplished'))['ClassroomObservation_Accomplished']
    January_IPMT.TOSRubrics_Accomplished = January_submissions.aggregate(TOSRubrics_Accomplished=Sum('TOSRubrics_Accomplished'))['TOSRubrics_Accomplished']
    January_IPMT.TestQuestions_Accomplished = January_submissions.aggregate(TestQuestions_Accomplished=Sum('TestQuestions_Accomplished'))['TestQuestions_Accomplished']
    January_IPMT.AnswerKey_Accomplished = January_submissions.aggregate(AnswerKey_Accomplished=Sum('AnswerKey_Accomplished'))['AnswerKey_Accomplished']
    January_IPMT.GradingSheet_Accomplished = January_submissions.aggregate(GradingSheet_Accomplished=Sum('GradingSheet_Accomplished'))['GradingSheet_Accomplished']
    January_IPMT.StudentAdviced_Accomplished = January_submissions.aggregate(StudentAdviced_Accomplished=Sum('StudentAdviced_Accomplished'))['StudentAdviced_Accomplished']
    January_IPMT.AccomplishmentReport_Accomplished = January_submissions.aggregate(AccomplishmentReport_Accomplished=Sum('AccomplishmentReport_Accomplished'))['AccomplishmentReport_Accomplished']
    January_IPMT.ResearchProposalSubmitted_Accomplished = January_submissions.aggregate(ResearchProposalSubmitted_Accomplished=Sum('ResearchProposalSubmitted_Accomplished'))['ResearchProposalSubmitted_Accomplished']
    January_IPMT.ResearchImplemented_Accomplished = January_submissions.aggregate(ResearchImplemented_Accomplished=Sum('ResearchImplemented_Accomplished'))['ResearchImplemented_Accomplished']
    January_IPMT.ResearchPresented_Accomplished = January_submissions.aggregate(ResearchPresented_Accomplished=Sum('ResearchPresented_Accomplished'))['ResearchPresented_Accomplished']
    January_IPMT.ResearchPublished_Accomplished = January_submissions.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
    January_IPMT.ApprovedIPRights_Accomplished = January_submissions.aggregate(ApprovedIPRights_Accomplished=Sum('ApprovedIPRights_Accomplished'))['ApprovedIPRights_Accomplished']
    January_IPMT.ResearchUtilized_Accomplished = January_submissions.aggregate(ResearchUtilized_Accomplished=Sum('ResearchUtilized_Accomplished'))['ResearchUtilized_Accomplished']
    January_IPMT.NumberOfCitations_Accomplished = January_submissions.aggregate(NumberOfCitations_Accomplished=Sum('NumberOfCitations_Accomplished'))['NumberOfCitations_Accomplished']
    January_IPMT.ExtensionProposalSubmitted_Accomplished = January_submissions.aggregate(ExtensionProposalSubmitted_Accomplished=Sum('ExtensionProposalSubmitted_Accomplished'))['ExtensionProposalSubmitted_Accomplished']
    January_IPMT.PersonTrained_Accomplished = January_submissions.aggregate(PersonTrained_Accomplished=Sum('PersonTrained_Accomplished'))['PersonTrained_Accomplished']
    January_IPMT.PersonAvailedRatedGood_Accomplished = January_submissions.aggregate(PersonAvailedRatedGood_Accomplished=Sum('PersonAvailedRatedGood_Accomplished'))['PersonAvailedRatedGood_Accomplished']
    January_IPMT.PersonTrainedRatedGood_Accomplished = January_submissions.aggregate(PersonTrainedRatedGood_Accomplished=Sum('PersonTrainedRatedGood_Accomplished'))['PersonTrainedRatedGood_Accomplished']
    January_IPMT.TechnicalAdvice_Accomplished = January_submissions.aggregate(TechnicalAdvice_Accomplished=Sum('TechnicalAdvice_Accomplished'))['TechnicalAdvice_Accomplished']
    January_IPMT.AccomplishmentReportDeligatedAssignment_Accomplished = January_submissions.aggregate(AccomplishmentReportDeligatedAssignment_Accomplished=Sum('AccomplishmentReportDeligatedAssignment_Accomplished'))['AccomplishmentReportDeligatedAssignment_Accomplished']
    January_IPMT.FlagRaisingAttendance_Accomplished = January_submissions.aggregate(FlagRaisingAttendance_Accomplished=Sum('FlagRaisingAttendance_Accomplished'))['FlagRaisingAttendance_Accomplished']
    January_IPMT.FlagLoweringAttendance_Accomplished = January_submissions.aggregate(FlagLoweringAttendance_Accomplished=Sum('FlagLoweringAttendance_Accomplished'))['FlagLoweringAttendance_Accomplished']
    January_IPMT.WellnessProgramAttendance_Accomplished = January_submissions.aggregate(WellnessProgramAttendance_Accomplished=Sum('WellnessProgramAttendance_Accomplished'))['WellnessProgramAttendance_Accomplished']
    January_IPMT.SchoolCelebrationAttendance_Accomplished = January_submissions.aggregate(SchoolCelebrationAttendance_Accomplished=Sum('SchoolCelebrationAttendance_Accomplished'))['SchoolCelebrationAttendance_Accomplished']
    January_IPMT.TrainingAttendance_Accomplished = January_submissions.aggregate(TrainingAttendance_Accomplished=Sum('TrainingAttendance_Accomplished'))['TrainingAttendance_Accomplished']
    January_IPMT.FacultyMeetingAttendance_Accomplished = January_submissions.aggregate(FacultyMeetingAttendance_Accomplished=Sum('FacultyMeetingAttendance_Accomplished'))['FacultyMeetingAttendance_Accomplished']
    January_IPMT.AccreditationAttendance_Accomplished = January_submissions.aggregate(AccreditationAttendance_Accomplished=Sum('AccreditationAttendance_Accomplished'))['AccreditationAttendance_Accomplished']
    January_IPMT.SpiritualActivityAttendance_Accomplished = January_submissions.aggregate(SpiritualActivityAttendance_Accomplished=Sum('SpiritualActivityAttendance_Accomplished'))['SpiritualActivityAttendance_Accomplished']
    January_IPMT.author = request.user
    January_IPMT.IPCR_Submitted = datetime.now().date()

    February_submissions = IPMT_Form_model.objects.filter(
        Q(author=current_user),
        Q(IPCR_Saved__month=month_feb),
        Q(IPCR_Saved__year=current_year),
    )
    
    February_IPMT.syllabus_Accomplished = February_submissions.aggregate(syllabus_Accomplished=Sum('syllabus_Accomplished'))['syllabus_Accomplished']
    February_IPMT.CourseGuide_Accomplished = February_submissions.aggregate(CourseGuide_Accomplished=Sum('CourseGuide_Accomplished'))['CourseGuide_Accomplished']
    February_IPMT.SLM_Accomplished = February_submissions.aggregate(SLM_Accomplished=Sum('SLM_Accomplished'))['SLM_Accomplished']
    February_IPMT.SubjectAreas_Accomplished = February_submissions.aggregate(SubjectAreas_Accomplished=Sum('SubjectAreas_Accomplished'))['SubjectAreas_Accomplished']
    February_IPMT.AttendanceSheet_Accomplished = February_submissions.aggregate(AttendanceSheet_Accomplished=Sum('AttendanceSheet_Accomplished'))['AttendanceSheet_Accomplished']
    February_IPMT.ClassRecord_Accomplished = February_submissions.aggregate(ClassRecord_Accomplished=Sum('ClassRecord_Accomplished'))['ClassRecord_Accomplished']
    February_IPMT.TeachingEffectiveness_Accomplished = February_submissions.aggregate(TeachingEffectiveness_Accomplished=Sum('TeachingEffectiveness_Accomplished'))['TeachingEffectiveness_Accomplished']
    February_IPMT.ClassroomObservation_Accomplished = February_submissions.aggregate(ClassroomObservation_Accomplished=Sum('ClassroomObservation_Accomplished'))['ClassroomObservation_Accomplished']
    February_IPMT.TOSRubrics_Accomplished = February_submissions.aggregate(TOSRubrics_Accomplished=Sum('TOSRubrics_Accomplished'))['TOSRubrics_Accomplished']
    February_IPMT.TestQuestions_Accomplished = February_submissions.aggregate(TestQuestions_Accomplished=Sum('TestQuestions_Accomplished'))['TestQuestions_Accomplished']
    February_IPMT.AnswerKey_Accomplished = February_submissions.aggregate(AnswerKey_Accomplished=Sum('AnswerKey_Accomplished'))['AnswerKey_Accomplished']
    February_IPMT.GradingSheet_Accomplished = February_submissions.aggregate(GradingSheet_Accomplished=Sum('GradingSheet_Accomplished'))['GradingSheet_Accomplished']
    February_IPMT.StudentAdviced_Accomplished = February_submissions.aggregate(StudentAdviced_Accomplished=Sum('StudentAdviced_Accomplished'))['StudentAdviced_Accomplished']
    February_IPMT.AccomplishmentReport_Accomplished = February_submissions.aggregate(AccomplishmentReport_Accomplished=Sum('AccomplishmentReport_Accomplished'))['AccomplishmentReport_Accomplished']
    February_IPMT.ResearchProposalSubmitted_Accomplished = February_submissions.aggregate(ResearchProposalSubmitted_Accomplished=Sum('ResearchProposalSubmitted_Accomplished'))['ResearchProposalSubmitted_Accomplished']
    February_IPMT.ResearchImplemented_Accomplished = February_submissions.aggregate(ResearchImplemented_Accomplished=Sum('ResearchImplemented_Accomplished'))['ResearchImplemented_Accomplished']
    February_IPMT.ResearchPresented_Accomplished = February_submissions.aggregate(ResearchPresented_Accomplished=Sum('ResearchPresented_Accomplished'))['ResearchPresented_Accomplished']
    February_IPMT.ResearchPublished_Accomplished = February_submissions.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
    February_IPMT.ApprovedIPRights_Accomplished = February_submissions.aggregate(ApprovedIPRights_Accomplished=Sum('ApprovedIPRights_Accomplished'))['ApprovedIPRights_Accomplished']
    February_IPMT.ResearchUtilized_Accomplished = February_submissions.aggregate(ResearchUtilized_Accomplished=Sum('ResearchUtilized_Accomplished'))['ResearchUtilized_Accomplished']
    February_IPMT.NumberOfCitations_Accomplished = February_submissions.aggregate(NumberOfCitations_Accomplished=Sum('NumberOfCitations_Accomplished'))['NumberOfCitations_Accomplished']
    February_IPMT.ExtensionProposalSubmitted_Accomplished = February_submissions.aggregate(ExtensionProposalSubmitted_Accomplished=Sum('ExtensionProposalSubmitted_Accomplished'))['ExtensionProposalSubmitted_Accomplished']
    February_IPMT.PersonTrained_Accomplished = February_submissions.aggregate(PersonTrained_Accomplished=Sum('PersonTrained_Accomplished'))['PersonTrained_Accomplished']
    February_IPMT.PersonAvailedRatedGood_Accomplished = February_submissions.aggregate(PersonAvailedRatedGood_Accomplished=Sum('PersonAvailedRatedGood_Accomplished'))['PersonAvailedRatedGood_Accomplished']
    February_IPMT.PersonTrainedRatedGood_Accomplished = February_submissions.aggregate(PersonTrainedRatedGood_Accomplished=Sum('PersonTrainedRatedGood_Accomplished'))['PersonTrainedRatedGood_Accomplished']
    February_IPMT.TechnicalAdvice_Accomplished = February_submissions.aggregate(TechnicalAdvice_Accomplished=Sum('TechnicalAdvice_Accomplished'))['TechnicalAdvice_Accomplished']
    February_IPMT.AccomplishmentReportDeligatedAssignment_Accomplished = February_submissions.aggregate(AccomplishmentReportDeligatedAssignment_Accomplished=Sum('AccomplishmentReportDeligatedAssignment_Accomplished'))['AccomplishmentReportDeligatedAssignment_Accomplished']
    February_IPMT.FlagRaisingAttendance_Accomplished = February_submissions.aggregate(FlagRaisingAttendance_Accomplished=Sum('FlagRaisingAttendance_Accomplished'))['FlagRaisingAttendance_Accomplished']
    February_IPMT.FlagLoweringAttendance_Accomplished = February_submissions.aggregate(FlagLoweringAttendance_Accomplished=Sum('FlagLoweringAttendance_Accomplished'))['FlagLoweringAttendance_Accomplished']
    February_IPMT.WellnessProgramAttendance_Accomplished = February_submissions.aggregate(WellnessProgramAttendance_Accomplished=Sum('WellnessProgramAttendance_Accomplished'))['WellnessProgramAttendance_Accomplished']
    February_IPMT.SchoolCelebrationAttendance_Accomplished = February_submissions.aggregate(SchoolCelebrationAttendance_Accomplished=Sum('SchoolCelebrationAttendance_Accomplished'))['SchoolCelebrationAttendance_Accomplished']
    February_IPMT.TrainingAttendance_Accomplished = February_submissions.aggregate(TrainingAttendance_Accomplished=Sum('TrainingAttendance_Accomplished'))['TrainingAttendance_Accomplished']
    February_IPMT.FacultyMeetingAttendance_Accomplished = February_submissions.aggregate(FacultyMeetingAttendance_Accomplished=Sum('FacultyMeetingAttendance_Accomplished'))['FacultyMeetingAttendance_Accomplished']
    February_IPMT.AccreditationAttendance_Accomplished = February_submissions.aggregate(AccreditationAttendance_Accomplished=Sum('AccreditationAttendance_Accomplished'))['AccreditationAttendance_Accomplished']
    February_IPMT.SpiritualActivityAttendance_Accomplished = February_submissions.aggregate(SpiritualActivityAttendance_Accomplished=Sum('SpiritualActivityAttendance_Accomplished'))['SpiritualActivityAttendance_Accomplished']
    February_IPMT.author = request.user
    February_IPMT.IPCR_Submitted = datetime.now().date()
    
    March_submissions = IPMT_Form_model.objects.filter(
        Q(author=current_user),
        Q(IPCR_Saved__month=month_mar),
        Q(IPCR_Saved__year=current_year),
    )
    
    March_IPMT.syllabus_Accomplished = March_submissions.aggregate(syllabus_Accomplished=Sum('syllabus_Accomplished'))['syllabus_Accomplished']
    March_IPMT.CourseGuide_Accomplished = March_submissions.aggregate(CourseGuide_Accomplished=Sum('CourseGuide_Accomplished'))['CourseGuide_Accomplished']
    March_IPMT.SLM_Accomplished = March_submissions.aggregate(SLM_Accomplished=Sum('SLM_Accomplished'))['SLM_Accomplished']
    March_IPMT.SubjectAreas_Accomplished = March_submissions.aggregate(SubjectAreas_Accomplished=Sum('SubjectAreas_Accomplished'))['SubjectAreas_Accomplished']
    March_IPMT.AttendanceSheet_Accomplished = March_submissions.aggregate(AttendanceSheet_Accomplished=Sum('AttendanceSheet_Accomplished'))['AttendanceSheet_Accomplished']
    March_IPMT.ClassRecord_Accomplished = March_submissions.aggregate(ClassRecord_Accomplished=Sum('ClassRecord_Accomplished'))['ClassRecord_Accomplished']
    March_IPMT.TeachingEffectiveness_Accomplished = March_submissions.aggregate(TeachingEffectiveness_Accomplished=Sum('TeachingEffectiveness_Accomplished'))['TeachingEffectiveness_Accomplished']
    March_IPMT.ClassroomObservation_Accomplished = March_submissions.aggregate(ClassroomObservation_Accomplished=Sum('ClassroomObservation_Accomplished'))['ClassroomObservation_Accomplished']
    March_IPMT.TOSRubrics_Accomplished = March_submissions.aggregate(TOSRubrics_Accomplished=Sum('TOSRubrics_Accomplished'))['TOSRubrics_Accomplished']
    March_IPMT.TestQuestions_Accomplished = March_submissions.aggregate(TestQuestions_Accomplished=Sum('TestQuestions_Accomplished'))['TestQuestions_Accomplished']
    March_IPMT.AnswerKey_Accomplished = March_submissions.aggregate(AnswerKey_Accomplished=Sum('AnswerKey_Accomplished'))['AnswerKey_Accomplished']
    March_IPMT.GradingSheet_Accomplished = March_submissions.aggregate(GradingSheet_Accomplished=Sum('GradingSheet_Accomplished'))['GradingSheet_Accomplished']
    March_IPMT.StudentAdviced_Accomplished = March_submissions.aggregate(StudentAdviced_Accomplished=Sum('StudentAdviced_Accomplished'))['StudentAdviced_Accomplished']
    March_IPMT.AccomplishmentReport_Accomplished = March_submissions.aggregate(AccomplishmentReport_Accomplished=Sum('AccomplishmentReport_Accomplished'))['AccomplishmentReport_Accomplished']
    March_IPMT.ResearchProposalSubmitted_Accomplished = March_submissions.aggregate(ResearchProposalSubmitted_Accomplished=Sum('ResearchProposalSubmitted_Accomplished'))['ResearchProposalSubmitted_Accomplished']
    March_IPMT.ResearchImplemented_Accomplished = March_submissions.aggregate(ResearchImplemented_Accomplished=Sum('ResearchImplemented_Accomplished'))['ResearchImplemented_Accomplished']
    March_IPMT.ResearchPresented_Accomplished = March_submissions.aggregate(ResearchPresented_Accomplished=Sum('ResearchPresented_Accomplished'))['ResearchPresented_Accomplished']
    March_IPMT.ResearchPublished_Accomplished = March_submissions.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
    March_IPMT.ApprovedIPRights_Accomplished = March_submissions.aggregate(ApprovedIPRights_Accomplished=Sum('ApprovedIPRights_Accomplished'))['ApprovedIPRights_Accomplished']
    March_IPMT.ResearchUtilized_Accomplished = March_submissions.aggregate(ResearchUtilized_Accomplished=Sum('ResearchUtilized_Accomplished'))['ResearchUtilized_Accomplished']
    March_IPMT.NumberOfCitations_Accomplished = March_submissions.aggregate(NumberOfCitations_Accomplished=Sum('NumberOfCitations_Accomplished'))['NumberOfCitations_Accomplished']
    March_IPMT.ExtensionProposalSubmitted_Accomplished = March_submissions.aggregate(ExtensionProposalSubmitted_Accomplished=Sum('ExtensionProposalSubmitted_Accomplished'))['ExtensionProposalSubmitted_Accomplished']
    March_IPMT.PersonTrained_Accomplished = March_submissions.aggregate(PersonTrained_Accomplished=Sum('PersonTrained_Accomplished'))['PersonTrained_Accomplished']
    March_IPMT.PersonAvailedRatedGood_Accomplished = March_submissions.aggregate(PersonAvailedRatedGood_Accomplished=Sum('PersonAvailedRatedGood_Accomplished'))['PersonAvailedRatedGood_Accomplished']
    March_IPMT.PersonTrainedRatedGood_Accomplished = March_submissions.aggregate(PersonTrainedRatedGood_Accomplished=Sum('PersonTrainedRatedGood_Accomplished'))['PersonTrainedRatedGood_Accomplished']
    March_IPMT.TechnicalAdvice_Accomplished = March_submissions.aggregate(TechnicalAdvice_Accomplished=Sum('TechnicalAdvice_Accomplished'))['TechnicalAdvice_Accomplished']
    March_IPMT.AccomplishmentReportDeligatedAssignment_Accomplished = March_submissions.aggregate(AccomplishmentReportDeligatedAssignment_Accomplished=Sum('AccomplishmentReportDeligatedAssignment_Accomplished'))['AccomplishmentReportDeligatedAssignment_Accomplished']
    March_IPMT.FlagRaisingAttendance_Accomplished = March_submissions.aggregate(FlagRaisingAttendance_Accomplished=Sum('FlagRaisingAttendance_Accomplished'))['FlagRaisingAttendance_Accomplished']
    March_IPMT.FlagLoweringAttendance_Accomplished = March_submissions.aggregate(FlagLoweringAttendance_Accomplished=Sum('FlagLoweringAttendance_Accomplished'))['FlagLoweringAttendance_Accomplished']
    March_IPMT.WellnessProgramAttendance_Accomplished = March_submissions.aggregate(WellnessProgramAttendance_Accomplished=Sum('WellnessProgramAttendance_Accomplished'))['WellnessProgramAttendance_Accomplished']
    March_IPMT.SchoolCelebrationAttendance_Accomplished = March_submissions.aggregate(SchoolCelebrationAttendance_Accomplished=Sum('SchoolCelebrationAttendance_Accomplished'))['SchoolCelebrationAttendance_Accomplished']
    March_IPMT.TrainingAttendance_Accomplished = March_submissions.aggregate(TrainingAttendance_Accomplished=Sum('TrainingAttendance_Accomplished'))['TrainingAttendance_Accomplished']
    March_IPMT.FacultyMeetingAttendance_Accomplished = March_submissions.aggregate(FacultyMeetingAttendance_Accomplished=Sum('FacultyMeetingAttendance_Accomplished'))['FacultyMeetingAttendance_Accomplished']
    March_IPMT.AccreditationAttendance_Accomplished = March_submissions.aggregate(AccreditationAttendance_Accomplished=Sum('AccreditationAttendance_Accomplished'))['AccreditationAttendance_Accomplished']
    March_IPMT.SpiritualActivityAttendance_Accomplished = March_submissions.aggregate(SpiritualActivityAttendance_Accomplished=Sum('SpiritualActivityAttendance_Accomplished'))['SpiritualActivityAttendance_Accomplished']
    March_IPMT.author = request.user
    March_IPMT.IPCR_Submitted = datetime.now().date()
    
    
    April_submissions = IPMT_Form_model.objects.filter(
        Q(author=current_user),
        Q(IPCR_Saved__month=month_apr),
        Q(IPCR_Saved__year=current_year),
    )
    
    April_IPMT.syllabus_Accomplished = April_submissions.aggregate(syllabus_Accomplished=Sum('syllabus_Accomplished'))['syllabus_Accomplished']
    April_IPMT.CourseGuide_Accomplished = April_submissions.aggregate(CourseGuide_Accomplished=Sum('CourseGuide_Accomplished'))['CourseGuide_Accomplished']
    April_IPMT.SLM_Accomplished = April_submissions.aggregate(SLM_Accomplished=Sum('SLM_Accomplished'))['SLM_Accomplished']
    April_IPMT.SubjectAreas_Accomplished = April_submissions.aggregate(SubjectAreas_Accomplished=Sum('SubjectAreas_Accomplished'))['SubjectAreas_Accomplished']
    April_IPMT.AttendanceSheet_Accomplished = April_submissions.aggregate(AttendanceSheet_Accomplished=Sum('AttendanceSheet_Accomplished'))['AttendanceSheet_Accomplished']
    April_IPMT.ClassRecord_Accomplished = April_submissions.aggregate(ClassRecord_Accomplished=Sum('ClassRecord_Accomplished'))['ClassRecord_Accomplished']
    April_IPMT.TeachingEffectiveness_Accomplished = April_submissions.aggregate(TeachingEffectiveness_Accomplished=Sum('TeachingEffectiveness_Accomplished'))['TeachingEffectiveness_Accomplished']
    April_IPMT.ClassroomObservation_Accomplished = April_submissions.aggregate(ClassroomObservation_Accomplished=Sum('ClassroomObservation_Accomplished'))['ClassroomObservation_Accomplished']
    April_IPMT.TOSRubrics_Accomplished = April_submissions.aggregate(TOSRubrics_Accomplished=Sum('TOSRubrics_Accomplished'))['TOSRubrics_Accomplished']
    April_IPMT.TestQuestions_Accomplished = April_submissions.aggregate(TestQuestions_Accomplished=Sum('TestQuestions_Accomplished'))['TestQuestions_Accomplished']
    April_IPMT.AnswerKey_Accomplished = April_submissions.aggregate(AnswerKey_Accomplished=Sum('AnswerKey_Accomplished'))['AnswerKey_Accomplished']
    April_IPMT.GradingSheet_Accomplished = April_submissions.aggregate(GradingSheet_Accomplished=Sum('GradingSheet_Accomplished'))['GradingSheet_Accomplished']
    April_IPMT.StudentAdviced_Accomplished = April_submissions.aggregate(StudentAdviced_Accomplished=Sum('StudentAdviced_Accomplished'))['StudentAdviced_Accomplished']
    April_IPMT.AccomplishmentReport_Accomplished = April_submissions.aggregate(AccomplishmentReport_Accomplished=Sum('AccomplishmentReport_Accomplished'))['AccomplishmentReport_Accomplished']
    April_IPMT.ResearchProposalSubmitted_Accomplished = April_submissions.aggregate(ResearchProposalSubmitted_Accomplished=Sum('ResearchProposalSubmitted_Accomplished'))['ResearchProposalSubmitted_Accomplished']
    April_IPMT.ResearchImplemented_Accomplished = April_submissions.aggregate(ResearchImplemented_Accomplished=Sum('ResearchImplemented_Accomplished'))['ResearchImplemented_Accomplished']
    April_IPMT.ResearchPresented_Accomplished = April_submissions.aggregate(ResearchPresented_Accomplished=Sum('ResearchPresented_Accomplished'))['ResearchPresented_Accomplished']
    April_IPMT.ResearchPublished_Accomplished = April_submissions.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
    April_IPMT.ApprovedIPRights_Accomplished = April_submissions.aggregate(ApprovedIPRights_Accomplished=Sum('ApprovedIPRights_Accomplished'))['ApprovedIPRights_Accomplished']
    April_IPMT.ResearchUtilized_Accomplished = April_submissions.aggregate(ResearchUtilized_Accomplished=Sum('ResearchUtilized_Accomplished'))['ResearchUtilized_Accomplished']
    April_IPMT.NumberOfCitations_Accomplished = April_submissions.aggregate(NumberOfCitations_Accomplished=Sum('NumberOfCitations_Accomplished'))['NumberOfCitations_Accomplished']
    April_IPMT.ExtensionProposalSubmitted_Accomplished = April_submissions.aggregate(ExtensionProposalSubmitted_Accomplished=Sum('ExtensionProposalSubmitted_Accomplished'))['ExtensionProposalSubmitted_Accomplished']
    April_IPMT.PersonTrained_Accomplished = April_submissions.aggregate(PersonTrained_Accomplished=Sum('PersonTrained_Accomplished'))['PersonTrained_Accomplished']
    April_IPMT.PersonAvailedRatedGood_Accomplished = April_submissions.aggregate(PersonAvailedRatedGood_Accomplished=Sum('PersonAvailedRatedGood_Accomplished'))['PersonAvailedRatedGood_Accomplished']
    April_IPMT.PersonTrainedRatedGood_Accomplished = April_submissions.aggregate(PersonTrainedRatedGood_Accomplished=Sum('PersonTrainedRatedGood_Accomplished'))['PersonTrainedRatedGood_Accomplished']
    April_IPMT.TechnicalAdvice_Accomplished = April_submissions.aggregate(TechnicalAdvice_Accomplished=Sum('TechnicalAdvice_Accomplished'))['TechnicalAdvice_Accomplished']
    April_IPMT.AccomplishmentReportDeligatedAssignment_Accomplished = April_submissions.aggregate(AccomplishmentReportDeligatedAssignment_Accomplished=Sum('AccomplishmentReportDeligatedAssignment_Accomplished'))['AccomplishmentReportDeligatedAssignment_Accomplished']
    April_IPMT.FlagRaisingAttendance_Accomplished = April_submissions.aggregate(FlagRaisingAttendance_Accomplished=Sum('FlagRaisingAttendance_Accomplished'))['FlagRaisingAttendance_Accomplished']
    April_IPMT.FlagLoweringAttendance_Accomplished = April_submissions.aggregate(FlagLoweringAttendance_Accomplished=Sum('FlagLoweringAttendance_Accomplished'))['FlagLoweringAttendance_Accomplished']
    April_IPMT.WellnessProgramAttendance_Accomplished = April_submissions.aggregate(WellnessProgramAttendance_Accomplished=Sum('WellnessProgramAttendance_Accomplished'))['WellnessProgramAttendance_Accomplished']
    April_IPMT.SchoolCelebrationAttendance_Accomplished = April_submissions.aggregate(SchoolCelebrationAttendance_Accomplished=Sum('SchoolCelebrationAttendance_Accomplished'))['SchoolCelebrationAttendance_Accomplished']
    April_IPMT.TrainingAttendance_Accomplished = April_submissions.aggregate(TrainingAttendance_Accomplished=Sum('TrainingAttendance_Accomplished'))['TrainingAttendance_Accomplished']
    April_IPMT.FacultyMeetingAttendance_Accomplished = April_submissions.aggregate(FacultyMeetingAttendance_Accomplished=Sum('FacultyMeetingAttendance_Accomplished'))['FacultyMeetingAttendance_Accomplished']
    April_IPMT.AccreditationAttendance_Accomplished = April_submissions.aggregate(AccreditationAttendance_Accomplished=Sum('AccreditationAttendance_Accomplished'))['AccreditationAttendance_Accomplished']
    April_IPMT.SpiritualActivityAttendance_Accomplished = April_submissions.aggregate(SpiritualActivityAttendance_Accomplished=Sum('SpiritualActivityAttendance_Accomplished'))['SpiritualActivityAttendance_Accomplished']
    April_IPMT.author = request.user
    April_IPMT.IPCR_Submitted = datetime.now().date()
    
    May_submissions = IPMT_Form_model.objects.filter(
        Q(author=current_user),
        Q(IPCR_Saved__month=month_may),
        Q(IPCR_Saved__year=current_year),
    )
    
    May_IPMT.syllabus_Accomplished = May_submissions.aggregate(syllabus_Accomplished=Sum('syllabus_Accomplished'))['syllabus_Accomplished']
    May_IPMT.CourseGuide_Accomplished = May_submissions.aggregate(CourseGuide_Accomplished=Sum('CourseGuide_Accomplished'))['CourseGuide_Accomplished']
    May_IPMT.SLM_Accomplished = May_submissions.aggregate(SLM_Accomplished=Sum('SLM_Accomplished'))['SLM_Accomplished']
    May_IPMT.SubjectAreas_Accomplished = May_submissions.aggregate(SubjectAreas_Accomplished=Sum('SubjectAreas_Accomplished'))['SubjectAreas_Accomplished']
    May_IPMT.AttendanceSheet_Accomplished = May_submissions.aggregate(AttendanceSheet_Accomplished=Sum('AttendanceSheet_Accomplished'))['AttendanceSheet_Accomplished']
    May_IPMT.ClassRecord_Accomplished = May_submissions.aggregate(ClassRecord_Accomplished=Sum('ClassRecord_Accomplished'))['ClassRecord_Accomplished']
    May_IPMT.TeachingEffectiveness_Accomplished = May_submissions.aggregate(TeachingEffectiveness_Accomplished=Sum('TeachingEffectiveness_Accomplished'))['TeachingEffectiveness_Accomplished']
    May_IPMT.ClassroomObservation_Accomplished = May_submissions.aggregate(ClassroomObservation_Accomplished=Sum('ClassroomObservation_Accomplished'))['ClassroomObservation_Accomplished']
    May_IPMT.TOSRubrics_Accomplished = May_submissions.aggregate(TOSRubrics_Accomplished=Sum('TOSRubrics_Accomplished'))['TOSRubrics_Accomplished']
    May_IPMT.TestQuestions_Accomplished = May_submissions.aggregate(TestQuestions_Accomplished=Sum('TestQuestions_Accomplished'))['TestQuestions_Accomplished']
    May_IPMT.AnswerKey_Accomplished = May_submissions.aggregate(AnswerKey_Accomplished=Sum('AnswerKey_Accomplished'))['AnswerKey_Accomplished']
    May_IPMT.GradingSheet_Accomplished = May_submissions.aggregate(GradingSheet_Accomplished=Sum('GradingSheet_Accomplished'))['GradingSheet_Accomplished']
    May_IPMT.StudentAdviced_Accomplished = May_submissions.aggregate(StudentAdviced_Accomplished=Sum('StudentAdviced_Accomplished'))['StudentAdviced_Accomplished']
    May_IPMT.AccomplishmentReport_Accomplished = May_submissions.aggregate(AccomplishmentReport_Accomplished=Sum('AccomplishmentReport_Accomplished'))['AccomplishmentReport_Accomplished']
    May_IPMT.ResearchProposalSubmitted_Accomplished = May_submissions.aggregate(ResearchProposalSubmitted_Accomplished=Sum('ResearchProposalSubmitted_Accomplished'))['ResearchProposalSubmitted_Accomplished']
    May_IPMT.ResearchImplemented_Accomplished = May_submissions.aggregate(ResearchImplemented_Accomplished=Sum('ResearchImplemented_Accomplished'))['ResearchImplemented_Accomplished']
    May_IPMT.ResearchPresented_Accomplished = May_submissions.aggregate(ResearchPresented_Accomplished=Sum('ResearchPresented_Accomplished'))['ResearchPresented_Accomplished']
    May_IPMT.ResearchPublished_Accomplished = May_submissions.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
    May_IPMT.ApprovedIPRights_Accomplished = May_submissions.aggregate(ApprovedIPRights_Accomplished=Sum('ApprovedIPRights_Accomplished'))['ApprovedIPRights_Accomplished']
    May_IPMT.ResearchUtilized_Accomplished = May_submissions.aggregate(ResearchUtilized_Accomplished=Sum('ResearchUtilized_Accomplished'))['ResearchUtilized_Accomplished']
    May_IPMT.NumberOfCitations_Accomplished = May_submissions.aggregate(NumberOfCitations_Accomplished=Sum('NumberOfCitations_Accomplished'))['NumberOfCitations_Accomplished']
    May_IPMT.ExtensionProposalSubmitted_Accomplished = May_submissions.aggregate(ExtensionProposalSubmitted_Accomplished=Sum('ExtensionProposalSubmitted_Accomplished'))['ExtensionProposalSubmitted_Accomplished']
    May_IPMT.PersonTrained_Accomplished = May_submissions.aggregate(PersonTrained_Accomplished=Sum('PersonTrained_Accomplished'))['PersonTrained_Accomplished']
    May_IPMT.PersonAvailedRatedGood_Accomplished = May_submissions.aggregate(PersonAvailedRatedGood_Accomplished=Sum('PersonAvailedRatedGood_Accomplished'))['PersonAvailedRatedGood_Accomplished']
    May_IPMT.PersonTrainedRatedGood_Accomplished = May_submissions.aggregate(PersonTrainedRatedGood_Accomplished=Sum('PersonTrainedRatedGood_Accomplished'))['PersonTrainedRatedGood_Accomplished']
    May_IPMT.TechnicalAdvice_Accomplished = May_submissions.aggregate(TechnicalAdvice_Accomplished=Sum('TechnicalAdvice_Accomplished'))['TechnicalAdvice_Accomplished']
    May_IPMT.AccomplishmentReportDeligatedAssignment_Accomplished = May_submissions.aggregate(AccomplishmentReportDeligatedAssignment_Accomplished=Sum('AccomplishmentReportDeligatedAssignment_Accomplished'))['AccomplishmentReportDeligatedAssignment_Accomplished']
    May_IPMT.FlagRaisingAttendance_Accomplished = May_submissions.aggregate(FlagRaisingAttendance_Accomplished=Sum('FlagRaisingAttendance_Accomplished'))['FlagRaisingAttendance_Accomplished']
    May_IPMT.FlagLoweringAttendance_Accomplished = May_submissions.aggregate(FlagLoweringAttendance_Accomplished=Sum('FlagLoweringAttendance_Accomplished'))['FlagLoweringAttendance_Accomplished']
    May_IPMT.WellnessProgramAttendance_Accomplished = May_submissions.aggregate(WellnessProgramAttendance_Accomplished=Sum('WellnessProgramAttendance_Accomplished'))['WellnessProgramAttendance_Accomplished']
    May_IPMT.SchoolCelebrationAttendance_Accomplished = May_submissions.aggregate(SchoolCelebrationAttendance_Accomplished=Sum('SchoolCelebrationAttendance_Accomplished'))['SchoolCelebrationAttendance_Accomplished']
    May_IPMT.TrainingAttendance_Accomplished = May_submissions.aggregate(TrainingAttendance_Accomplished=Sum('TrainingAttendance_Accomplished'))['TrainingAttendance_Accomplished']
    May_IPMT.FacultyMeetingAttendance_Accomplished = May_submissions.aggregate(FacultyMeetingAttendance_Accomplished=Sum('FacultyMeetingAttendance_Accomplished'))['FacultyMeetingAttendance_Accomplished']
    May_IPMT.AccreditationAttendance_Accomplished = May_submissions.aggregate(AccreditationAttendance_Accomplished=Sum('AccreditationAttendance_Accomplished'))['AccreditationAttendance_Accomplished']
    May_IPMT.SpiritualActivityAttendance_Accomplished = May_submissions.aggregate(SpiritualActivityAttendance_Accomplished=Sum('SpiritualActivityAttendance_Accomplished'))['SpiritualActivityAttendance_Accomplished']
    May_IPMT.author = request.user
    May_IPMT.IPCR_Submitted = datetime.now().date()
    
    June_submissions = IPMT_Form_model.objects.filter(
        Q(author=current_user),
        Q(IPCR_Saved__month=month_jun),
        Q(IPCR_Saved__year=current_year),
    )
    
    June_IPMT.syllabus_Accomplished = June_submissions.aggregate(syllabus_Accomplished=Sum('syllabus_Accomplished'))['syllabus_Accomplished']
    June_IPMT.CourseGuide_Accomplished = June_submissions.aggregate(CourseGuide_Accomplished=Sum('CourseGuide_Accomplished'))['CourseGuide_Accomplished']
    June_IPMT.SLM_Accomplished = June_submissions.aggregate(SLM_Accomplished=Sum('SLM_Accomplished'))['SLM_Accomplished']
    June_IPMT.SubjectAreas_Accomplished = June_submissions.aggregate(SubjectAreas_Accomplished=Sum('SubjectAreas_Accomplished'))['SubjectAreas_Accomplished']
    June_IPMT.AttendanceSheet_Accomplished = June_submissions.aggregate(AttendanceSheet_Accomplished=Sum('AttendanceSheet_Accomplished'))['AttendanceSheet_Accomplished']
    June_IPMT.ClassRecord_Accomplished = June_submissions.aggregate(ClassRecord_Accomplished=Sum('ClassRecord_Accomplished'))['ClassRecord_Accomplished']
    June_IPMT.TeachingEffectiveness_Accomplished = June_submissions.aggregate(TeachingEffectiveness_Accomplished=Sum('TeachingEffectiveness_Accomplished'))['TeachingEffectiveness_Accomplished']
    June_IPMT.ClassroomObservation_Accomplished = June_submissions.aggregate(ClassroomObservation_Accomplished=Sum('ClassroomObservation_Accomplished'))['ClassroomObservation_Accomplished']
    June_IPMT.TOSRubrics_Accomplished = June_submissions.aggregate(TOSRubrics_Accomplished=Sum('TOSRubrics_Accomplished'))['TOSRubrics_Accomplished']
    June_IPMT.TestQuestions_Accomplished = June_submissions.aggregate(TestQuestions_Accomplished=Sum('TestQuestions_Accomplished'))['TestQuestions_Accomplished']
    June_IPMT.AnswerKey_Accomplished = June_submissions.aggregate(AnswerKey_Accomplished=Sum('AnswerKey_Accomplished'))['AnswerKey_Accomplished']
    June_IPMT.GradingSheet_Accomplished = June_submissions.aggregate(GradingSheet_Accomplished=Sum('GradingSheet_Accomplished'))['GradingSheet_Accomplished']
    June_IPMT.StudentAdviced_Accomplished = June_submissions.aggregate(StudentAdviced_Accomplished=Sum('StudentAdviced_Accomplished'))['StudentAdviced_Accomplished']
    June_IPMT.AccomplishmentReport_Accomplished = June_submissions.aggregate(AccomplishmentReport_Accomplished=Sum('AccomplishmentReport_Accomplished'))['AccomplishmentReport_Accomplished']
    June_IPMT.ResearchProposalSubmitted_Accomplished = June_submissions.aggregate(ResearchProposalSubmitted_Accomplished=Sum('ResearchProposalSubmitted_Accomplished'))['ResearchProposalSubmitted_Accomplished']
    June_IPMT.ResearchImplemented_Accomplished = June_submissions.aggregate(ResearchImplemented_Accomplished=Sum('ResearchImplemented_Accomplished'))['ResearchImplemented_Accomplished']
    June_IPMT.ResearchPresented_Accomplished = June_submissions.aggregate(ResearchPresented_Accomplished=Sum('ResearchPresented_Accomplished'))['ResearchPresented_Accomplished']
    June_IPMT.ResearchPublished_Accomplished = June_submissions.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
    June_IPMT.ApprovedIPRights_Accomplished = June_submissions.aggregate(ApprovedIPRights_Accomplished=Sum('ApprovedIPRights_Accomplished'))['ApprovedIPRights_Accomplished']
    June_IPMT.ResearchUtilized_Accomplished = June_submissions.aggregate(ResearchUtilized_Accomplished=Sum('ResearchUtilized_Accomplished'))['ResearchUtilized_Accomplished']
    June_IPMT.NumberOfCitations_Accomplished = June_submissions.aggregate(NumberOfCitations_Accomplished=Sum('NumberOfCitations_Accomplished'))['NumberOfCitations_Accomplished']
    June_IPMT.ExtensionProposalSubmitted_Accomplished = June_submissions.aggregate(ExtensionProposalSubmitted_Accomplished=Sum('ExtensionProposalSubmitted_Accomplished'))['ExtensionProposalSubmitted_Accomplished']
    June_IPMT.PersonTrained_Accomplished = June_submissions.aggregate(PersonTrained_Accomplished=Sum('PersonTrained_Accomplished'))['PersonTrained_Accomplished']
    June_IPMT.PersonAvailedRatedGood_Accomplished = June_submissions.aggregate(PersonAvailedRatedGood_Accomplished=Sum('PersonAvailedRatedGood_Accomplished'))['PersonAvailedRatedGood_Accomplished']
    June_IPMT.PersonTrainedRatedGood_Accomplished = June_submissions.aggregate(PersonTrainedRatedGood_Accomplished=Sum('PersonTrainedRatedGood_Accomplished'))['PersonTrainedRatedGood_Accomplished']
    June_IPMT.TechnicalAdvice_Accomplished = June_submissions.aggregate(TechnicalAdvice_Accomplished=Sum('TechnicalAdvice_Accomplished'))['TechnicalAdvice_Accomplished']
    June_IPMT.AccomplishmentReportDeligatedAssignment_Accomplished = June_submissions.aggregate(AccomplishmentReportDeligatedAssignment_Accomplished=Sum('AccomplishmentReportDeligatedAssignment_Accomplished'))['AccomplishmentReportDeligatedAssignment_Accomplished']
    June_IPMT.FlagRaisingAttendance_Accomplished = June_submissions.aggregate(FlagRaisingAttendance_Accomplished=Sum('FlagRaisingAttendance_Accomplished'))['FlagRaisingAttendance_Accomplished']
    June_IPMT.FlagLoweringAttendance_Accomplished = June_submissions.aggregate(FlagLoweringAttendance_Accomplished=Sum('FlagLoweringAttendance_Accomplished'))['FlagLoweringAttendance_Accomplished']
    June_IPMT.WellnessProgramAttendance_Accomplished = June_submissions.aggregate(WellnessProgramAttendance_Accomplished=Sum('WellnessProgramAttendance_Accomplished'))['WellnessProgramAttendance_Accomplished']
    June_IPMT.SchoolCelebrationAttendance_Accomplished = June_submissions.aggregate(SchoolCelebrationAttendance_Accomplished=Sum('SchoolCelebrationAttendance_Accomplished'))['SchoolCelebrationAttendance_Accomplished']
    June_IPMT.TrainingAttendance_Accomplished = June_submissions.aggregate(TrainingAttendance_Accomplished=Sum('TrainingAttendance_Accomplished'))['TrainingAttendance_Accomplished']
    June_IPMT.FacultyMeetingAttendance_Accomplished = June_submissions.aggregate(FacultyMeetingAttendance_Accomplished=Sum('FacultyMeetingAttendance_Accomplished'))['FacultyMeetingAttendance_Accomplished']
    June_IPMT.AccreditationAttendance_Accomplished = June_submissions.aggregate(AccreditationAttendance_Accomplished=Sum('AccreditationAttendance_Accomplished'))['AccreditationAttendance_Accomplished']
    June_IPMT.SpiritualActivityAttendance_Accomplished = June_submissions.aggregate(SpiritualActivityAttendance_Accomplished=Sum('SpiritualActivityAttendance_Accomplished'))['SpiritualActivityAttendance_Accomplished']
    June_IPMT.author = request.user
    June_IPMT.IPCR_Submitted = datetime.now().date()
    
    July_submissions = IPMT_Form_model.objects.filter(
        Q(author=current_user),
        Q(IPCR_Saved__month=month_jul),
        Q(IPCR_Saved__year=current_year),
    )
    
    July_IPMT.syllabus_Accomplished = July_submissions.aggregate(syllabus_Accomplished=Sum('syllabus_Accomplished'))['syllabus_Accomplished']
    July_IPMT.CourseGuide_Accomplished = July_submissions.aggregate(CourseGuide_Accomplished=Sum('CourseGuide_Accomplished'))['CourseGuide_Accomplished']
    July_IPMT.SLM_Accomplished = July_submissions.aggregate(SLM_Accomplished=Sum('SLM_Accomplished'))['SLM_Accomplished']
    July_IPMT.SubjectAreas_Accomplished = July_submissions.aggregate(SubjectAreas_Accomplished=Sum('SubjectAreas_Accomplished'))['SubjectAreas_Accomplished']
    July_IPMT.AttendanceSheet_Accomplished = July_submissions.aggregate(AttendanceSheet_Accomplished=Sum('AttendanceSheet_Accomplished'))['AttendanceSheet_Accomplished']
    July_IPMT.ClassRecord_Accomplished = July_submissions.aggregate(ClassRecord_Accomplished=Sum('ClassRecord_Accomplished'))['ClassRecord_Accomplished']
    July_IPMT.TeachingEffectiveness_Accomplished = July_submissions.aggregate(TeachingEffectiveness_Accomplished=Sum('TeachingEffectiveness_Accomplished'))['TeachingEffectiveness_Accomplished']
    July_IPMT.ClassroomObservation_Accomplished = July_submissions.aggregate(ClassroomObservation_Accomplished=Sum('ClassroomObservation_Accomplished'))['ClassroomObservation_Accomplished']
    July_IPMT.TOSRubrics_Accomplished = July_submissions.aggregate(TOSRubrics_Accomplished=Sum('TOSRubrics_Accomplished'))['TOSRubrics_Accomplished']
    July_IPMT.TestQuestions_Accomplished = July_submissions.aggregate(TestQuestions_Accomplished=Sum('TestQuestions_Accomplished'))['TestQuestions_Accomplished']
    July_IPMT.AnswerKey_Accomplished = July_submissions.aggregate(AnswerKey_Accomplished=Sum('AnswerKey_Accomplished'))['AnswerKey_Accomplished']
    July_IPMT.GradingSheet_Accomplished = July_submissions.aggregate(GradingSheet_Accomplished=Sum('GradingSheet_Accomplished'))['GradingSheet_Accomplished']
    July_IPMT.StudentAdviced_Accomplished = July_submissions.aggregate(StudentAdviced_Accomplished=Sum('StudentAdviced_Accomplished'))['StudentAdviced_Accomplished']
    July_IPMT.AccomplishmentReport_Accomplished = July_submissions.aggregate(AccomplishmentReport_Accomplished=Sum('AccomplishmentReport_Accomplished'))['AccomplishmentReport_Accomplished']
    July_IPMT.ResearchProposalSubmitted_Accomplished = July_submissions.aggregate(ResearchProposalSubmitted_Accomplished=Sum('ResearchProposalSubmitted_Accomplished'))['ResearchProposalSubmitted_Accomplished']
    July_IPMT.ResearchImplemented_Accomplished = July_submissions.aggregate(ResearchImplemented_Accomplished=Sum('ResearchImplemented_Accomplished'))['ResearchImplemented_Accomplished']
    July_IPMT.ResearchPresented_Accomplished = July_submissions.aggregate(ResearchPresented_Accomplished=Sum('ResearchPresented_Accomplished'))['ResearchPresented_Accomplished']
    July_IPMT.ResearchPublished_Accomplished = July_submissions.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
    July_IPMT.ApprovedIPRights_Accomplished = July_submissions.aggregate(ApprovedIPRights_Accomplished=Sum('ApprovedIPRights_Accomplished'))['ApprovedIPRights_Accomplished']
    July_IPMT.ResearchUtilized_Accomplished = July_submissions.aggregate(ResearchUtilized_Accomplished=Sum('ResearchUtilized_Accomplished'))['ResearchUtilized_Accomplished']
    July_IPMT.NumberOfCitations_Accomplished = July_submissions.aggregate(NumberOfCitations_Accomplished=Sum('NumberOfCitations_Accomplished'))['NumberOfCitations_Accomplished']
    July_IPMT.ExtensionProposalSubmitted_Accomplished = July_submissions.aggregate(ExtensionProposalSubmitted_Accomplished=Sum('ExtensionProposalSubmitted_Accomplished'))['ExtensionProposalSubmitted_Accomplished']
    July_IPMT.PersonTrained_Accomplished = July_submissions.aggregate(PersonTrained_Accomplished=Sum('PersonTrained_Accomplished'))['PersonTrained_Accomplished']
    July_IPMT.PersonAvailedRatedGood_Accomplished = July_submissions.aggregate(PersonAvailedRatedGood_Accomplished=Sum('PersonAvailedRatedGood_Accomplished'))['PersonAvailedRatedGood_Accomplished']
    July_IPMT.PersonTrainedRatedGood_Accomplished = July_submissions.aggregate(PersonTrainedRatedGood_Accomplished=Sum('PersonTrainedRatedGood_Accomplished'))['PersonTrainedRatedGood_Accomplished']
    July_IPMT.TechnicalAdvice_Accomplished = July_submissions.aggregate(TechnicalAdvice_Accomplished=Sum('TechnicalAdvice_Accomplished'))['TechnicalAdvice_Accomplished']
    July_IPMT.AccomplishmentReportDeligatedAssignment_Accomplished = July_submissions.aggregate(AccomplishmentReportDeligatedAssignment_Accomplished=Sum('AccomplishmentReportDeligatedAssignment_Accomplished'))['AccomplishmentReportDeligatedAssignment_Accomplished']
    July_IPMT.FlagRaisingAttendance_Accomplished = July_submissions.aggregate(FlagRaisingAttendance_Accomplished=Sum('FlagRaisingAttendance_Accomplished'))['FlagRaisingAttendance_Accomplished']
    July_IPMT.FlagLoweringAttendance_Accomplished = July_submissions.aggregate(FlagLoweringAttendance_Accomplished=Sum('FlagLoweringAttendance_Accomplished'))['FlagLoweringAttendance_Accomplished']
    July_IPMT.WellnessProgramAttendance_Accomplished = July_submissions.aggregate(WellnessProgramAttendance_Accomplished=Sum('WellnessProgramAttendance_Accomplished'))['WellnessProgramAttendance_Accomplished']
    July_IPMT.SchoolCelebrationAttendance_Accomplished = July_submissions.aggregate(SchoolCelebrationAttendance_Accomplished=Sum('SchoolCelebrationAttendance_Accomplished'))['SchoolCelebrationAttendance_Accomplished']
    July_IPMT.TrainingAttendance_Accomplished = July_submissions.aggregate(TrainingAttendance_Accomplished=Sum('TrainingAttendance_Accomplished'))['TrainingAttendance_Accomplished']
    July_IPMT.FacultyMeetingAttendance_Accomplished = July_submissions.aggregate(FacultyMeetingAttendance_Accomplished=Sum('FacultyMeetingAttendance_Accomplished'))['FacultyMeetingAttendance_Accomplished']
    July_IPMT.AccreditationAttendance_Accomplished = July_submissions.aggregate(AccreditationAttendance_Accomplished=Sum('AccreditationAttendance_Accomplished'))['AccreditationAttendance_Accomplished']
    July_IPMT.SpiritualActivityAttendance_Accomplished = July_submissions.aggregate(SpiritualActivityAttendance_Accomplished=Sum('SpiritualActivityAttendance_Accomplished'))['SpiritualActivityAttendance_Accomplished']
    July_IPMT.author = request.user
    July_IPMT.IPCR_Submitted = datetime.now().date()
    
    August_submissions = IPMT_Form_model.objects.filter(
        Q(author=current_user),
        Q(IPCR_Saved__month=month_aug),
        Q(IPCR_Saved__year=current_year),
    )
    
    August_IPMT.syllabus_Accomplished = August_submissions.aggregate(syllabus_Accomplished=Sum('syllabus_Accomplished'))['syllabus_Accomplished']
    August_IPMT.CourseGuide_Accomplished = August_submissions.aggregate(CourseGuide_Accomplished=Sum('CourseGuide_Accomplished'))['CourseGuide_Accomplished']
    August_IPMT.SLM_Accomplished = August_submissions.aggregate(SLM_Accomplished=Sum('SLM_Accomplished'))['SLM_Accomplished']
    August_IPMT.SubjectAreas_Accomplished = August_submissions.aggregate(SubjectAreas_Accomplished=Sum('SubjectAreas_Accomplished'))['SubjectAreas_Accomplished']
    August_IPMT.AttendanceSheet_Accomplished = August_submissions.aggregate(AttendanceSheet_Accomplished=Sum('AttendanceSheet_Accomplished'))['AttendanceSheet_Accomplished']
    August_IPMT.ClassRecord_Accomplished = August_submissions.aggregate(ClassRecord_Accomplished=Sum('ClassRecord_Accomplished'))['ClassRecord_Accomplished']
    August_IPMT.TeachingEffectiveness_Accomplished = August_submissions.aggregate(TeachingEffectiveness_Accomplished=Sum('TeachingEffectiveness_Accomplished'))['TeachingEffectiveness_Accomplished']
    August_IPMT.ClassroomObservation_Accomplished = August_submissions.aggregate(ClassroomObservation_Accomplished=Sum('ClassroomObservation_Accomplished'))['ClassroomObservation_Accomplished']
    August_IPMT.TOSRubrics_Accomplished = August_submissions.aggregate(TOSRubrics_Accomplished=Sum('TOSRubrics_Accomplished'))['TOSRubrics_Accomplished']
    August_IPMT.TestQuestions_Accomplished = August_submissions.aggregate(TestQuestions_Accomplished=Sum('TestQuestions_Accomplished'))['TestQuestions_Accomplished']
    August_IPMT.AnswerKey_Accomplished = August_submissions.aggregate(AnswerKey_Accomplished=Sum('AnswerKey_Accomplished'))['AnswerKey_Accomplished']
    August_IPMT.GradingSheet_Accomplished = August_submissions.aggregate(GradingSheet_Accomplished=Sum('GradingSheet_Accomplished'))['GradingSheet_Accomplished']
    August_IPMT.StudentAdviced_Accomplished = August_submissions.aggregate(StudentAdviced_Accomplished=Sum('StudentAdviced_Accomplished'))['StudentAdviced_Accomplished']
    August_IPMT.AccomplishmentReport_Accomplished = August_submissions.aggregate(AccomplishmentReport_Accomplished=Sum('AccomplishmentReport_Accomplished'))['AccomplishmentReport_Accomplished']
    August_IPMT.ResearchProposalSubmitted_Accomplished = August_submissions.aggregate(ResearchProposalSubmitted_Accomplished=Sum('ResearchProposalSubmitted_Accomplished'))['ResearchProposalSubmitted_Accomplished']
    August_IPMT.ResearchImplemented_Accomplished = August_submissions.aggregate(ResearchImplemented_Accomplished=Sum('ResearchImplemented_Accomplished'))['ResearchImplemented_Accomplished']
    August_IPMT.ResearchPresented_Accomplished = August_submissions.aggregate(ResearchPresented_Accomplished=Sum('ResearchPresented_Accomplished'))['ResearchPresented_Accomplished']
    August_IPMT.ResearchPublished_Accomplished = August_submissions.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
    August_IPMT.ApprovedIPRights_Accomplished = August_submissions.aggregate(ApprovedIPRights_Accomplished=Sum('ApprovedIPRights_Accomplished'))['ApprovedIPRights_Accomplished']
    August_IPMT.ResearchUtilized_Accomplished = August_submissions.aggregate(ResearchUtilized_Accomplished=Sum('ResearchUtilized_Accomplished'))['ResearchUtilized_Accomplished']
    August_IPMT.NumberOfCitations_Accomplished = August_submissions.aggregate(NumberOfCitations_Accomplished=Sum('NumberOfCitations_Accomplished'))['NumberOfCitations_Accomplished']
    August_IPMT.ExtensionProposalSubmitted_Accomplished = August_submissions.aggregate(ExtensionProposalSubmitted_Accomplished=Sum('ExtensionProposalSubmitted_Accomplished'))['ExtensionProposalSubmitted_Accomplished']
    August_IPMT.PersonTrained_Accomplished = August_submissions.aggregate(PersonTrained_Accomplished=Sum('PersonTrained_Accomplished'))['PersonTrained_Accomplished']
    August_IPMT.PersonAvailedRatedGood_Accomplished = August_submissions.aggregate(PersonAvailedRatedGood_Accomplished=Sum('PersonAvailedRatedGood_Accomplished'))['PersonAvailedRatedGood_Accomplished']
    August_IPMT.PersonTrainedRatedGood_Accomplished = August_submissions.aggregate(PersonTrainedRatedGood_Accomplished=Sum('PersonTrainedRatedGood_Accomplished'))['PersonTrainedRatedGood_Accomplished']
    August_IPMT.TechnicalAdvice_Accomplished = August_submissions.aggregate(TechnicalAdvice_Accomplished=Sum('TechnicalAdvice_Accomplished'))['TechnicalAdvice_Accomplished']
    August_IPMT.AccomplishmentReportDeligatedAssignment_Accomplished = August_submissions.aggregate(AccomplishmentReportDeligatedAssignment_Accomplished=Sum('AccomplishmentReportDeligatedAssignment_Accomplished'))['AccomplishmentReportDeligatedAssignment_Accomplished']
    August_IPMT.FlagRaisingAttendance_Accomplished = August_submissions.aggregate(FlagRaisingAttendance_Accomplished=Sum('FlagRaisingAttendance_Accomplished'))['FlagRaisingAttendance_Accomplished']
    August_IPMT.FlagLoweringAttendance_Accomplished = August_submissions.aggregate(FlagLoweringAttendance_Accomplished=Sum('FlagLoweringAttendance_Accomplished'))['FlagLoweringAttendance_Accomplished']
    August_IPMT.WellnessProgramAttendance_Accomplished = August_submissions.aggregate(WellnessProgramAttendance_Accomplished=Sum('WellnessProgramAttendance_Accomplished'))['WellnessProgramAttendance_Accomplished']
    August_IPMT.SchoolCelebrationAttendance_Accomplished = August_submissions.aggregate(SchoolCelebrationAttendance_Accomplished=Sum('SchoolCelebrationAttendance_Accomplished'))['SchoolCelebrationAttendance_Accomplished']
    August_IPMT.TrainingAttendance_Accomplished = August_submissions.aggregate(TrainingAttendance_Accomplished=Sum('TrainingAttendance_Accomplished'))['TrainingAttendance_Accomplished']
    August_IPMT.FacultyMeetingAttendance_Accomplished = August_submissions.aggregate(FacultyMeetingAttendance_Accomplished=Sum('FacultyMeetingAttendance_Accomplished'))['FacultyMeetingAttendance_Accomplished']
    August_IPMT.AccreditationAttendance_Accomplished = August_submissions.aggregate(AccreditationAttendance_Accomplished=Sum('AccreditationAttendance_Accomplished'))['AccreditationAttendance_Accomplished']
    August_IPMT.SpiritualActivityAttendance_Accomplished = August_submissions.aggregate(SpiritualActivityAttendance_Accomplished=Sum('SpiritualActivityAttendance_Accomplished'))['SpiritualActivityAttendance_Accomplished']
    August_IPMT.author = request.user
    August_IPMT.IPCR_Submitted = datetime.now().date()
    
    September_submissions = IPMT_Form_model.objects.filter(
        Q(author=current_user),
        Q(IPCR_Saved__month=month_sep),
        Q(IPCR_Saved__year=current_year),
    )
    
    September_IPMT.syllabus_Accomplished = September_submissions.aggregate(syllabus_Accomplished=Sum('syllabus_Accomplished'))['syllabus_Accomplished']
    September_IPMT.CourseGuide_Accomplished = September_submissions.aggregate(CourseGuide_Accomplished=Sum('CourseGuide_Accomplished'))['CourseGuide_Accomplished']
    September_IPMT.SLM_Accomplished = September_submissions.aggregate(SLM_Accomplished=Sum('SLM_Accomplished'))['SLM_Accomplished']
    September_IPMT.SubjectAreas_Accomplished = September_submissions.aggregate(SubjectAreas_Accomplished=Sum('SubjectAreas_Accomplished'))['SubjectAreas_Accomplished']
    September_IPMT.AttendanceSheet_Accomplished = September_submissions.aggregate(AttendanceSheet_Accomplished=Sum('AttendanceSheet_Accomplished'))['AttendanceSheet_Accomplished']
    September_IPMT.ClassRecord_Accomplished = September_submissions.aggregate(ClassRecord_Accomplished=Sum('ClassRecord_Accomplished'))['ClassRecord_Accomplished']
    September_IPMT.TeachingEffectiveness_Accomplished = September_submissions.aggregate(TeachingEffectiveness_Accomplished=Sum('TeachingEffectiveness_Accomplished'))['TeachingEffectiveness_Accomplished']
    September_IPMT.ClassroomObservation_Accomplished = September_submissions.aggregate(ClassroomObservation_Accomplished=Sum('ClassroomObservation_Accomplished'))['ClassroomObservation_Accomplished']
    September_IPMT.TOSRubrics_Accomplished = September_submissions.aggregate(TOSRubrics_Accomplished=Sum('TOSRubrics_Accomplished'))['TOSRubrics_Accomplished']
    September_IPMT.TestQuestions_Accomplished = September_submissions.aggregate(TestQuestions_Accomplished=Sum('TestQuestions_Accomplished'))['TestQuestions_Accomplished']
    September_IPMT.AnswerKey_Accomplished = September_submissions.aggregate(AnswerKey_Accomplished=Sum('AnswerKey_Accomplished'))['AnswerKey_Accomplished']
    September_IPMT.GradingSheet_Accomplished = September_submissions.aggregate(GradingSheet_Accomplished=Sum('GradingSheet_Accomplished'))['GradingSheet_Accomplished']
    September_IPMT.StudentAdviced_Accomplished = September_submissions.aggregate(StudentAdviced_Accomplished=Sum('StudentAdviced_Accomplished'))['StudentAdviced_Accomplished']
    September_IPMT.AccomplishmentReport_Accomplished = September_submissions.aggregate(AccomplishmentReport_Accomplished=Sum('AccomplishmentReport_Accomplished'))['AccomplishmentReport_Accomplished']
    September_IPMT.ResearchProposalSubmitted_Accomplished = September_submissions.aggregate(ResearchProposalSubmitted_Accomplished=Sum('ResearchProposalSubmitted_Accomplished'))['ResearchProposalSubmitted_Accomplished']
    September_IPMT.ResearchImplemented_Accomplished = September_submissions.aggregate(ResearchImplemented_Accomplished=Sum('ResearchImplemented_Accomplished'))['ResearchImplemented_Accomplished']
    September_IPMT.ResearchPresented_Accomplished = September_submissions.aggregate(ResearchPresented_Accomplished=Sum('ResearchPresented_Accomplished'))['ResearchPresented_Accomplished']
    September_IPMT.ResearchPublished_Accomplished = September_submissions.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
    September_IPMT.ApprovedIPRights_Accomplished = September_submissions.aggregate(ApprovedIPRights_Accomplished=Sum('ApprovedIPRights_Accomplished'))['ApprovedIPRights_Accomplished']
    September_IPMT.ResearchUtilized_Accomplished = September_submissions.aggregate(ResearchUtilized_Accomplished=Sum('ResearchUtilized_Accomplished'))['ResearchUtilized_Accomplished']
    September_IPMT.NumberOfCitations_Accomplished = September_submissions.aggregate(NumberOfCitations_Accomplished=Sum('NumberOfCitations_Accomplished'))['NumberOfCitations_Accomplished']
    September_IPMT.ExtensionProposalSubmitted_Accomplished = September_submissions.aggregate(ExtensionProposalSubmitted_Accomplished=Sum('ExtensionProposalSubmitted_Accomplished'))['ExtensionProposalSubmitted_Accomplished']
    September_IPMT.PersonTrained_Accomplished = September_submissions.aggregate(PersonTrained_Accomplished=Sum('PersonTrained_Accomplished'))['PersonTrained_Accomplished']
    September_IPMT.PersonAvailedRatedGood_Accomplished = September_submissions.aggregate(PersonAvailedRatedGood_Accomplished=Sum('PersonAvailedRatedGood_Accomplished'))['PersonAvailedRatedGood_Accomplished']
    September_IPMT.PersonTrainedRatedGood_Accomplished = September_submissions.aggregate(PersonTrainedRatedGood_Accomplished=Sum('PersonTrainedRatedGood_Accomplished'))['PersonTrainedRatedGood_Accomplished']
    September_IPMT.TechnicalAdvice_Accomplished = September_submissions.aggregate(TechnicalAdvice_Accomplished=Sum('TechnicalAdvice_Accomplished'))['TechnicalAdvice_Accomplished']
    September_IPMT.AccomplishmentReportDeligatedAssignment_Accomplished = September_submissions.aggregate(AccomplishmentReportDeligatedAssignment_Accomplished=Sum('AccomplishmentReportDeligatedAssignment_Accomplished'))['AccomplishmentReportDeligatedAssignment_Accomplished']
    September_IPMT.FlagRaisingAttendance_Accomplished = September_submissions.aggregate(FlagRaisingAttendance_Accomplished=Sum('FlagRaisingAttendance_Accomplished'))['FlagRaisingAttendance_Accomplished']
    September_IPMT.FlagLoweringAttendance_Accomplished = September_submissions.aggregate(FlagLoweringAttendance_Accomplished=Sum('FlagLoweringAttendance_Accomplished'))['FlagLoweringAttendance_Accomplished']
    September_IPMT.WellnessProgramAttendance_Accomplished = September_submissions.aggregate(WellnessProgramAttendance_Accomplished=Sum('WellnessProgramAttendance_Accomplished'))['WellnessProgramAttendance_Accomplished']
    September_IPMT.SchoolCelebrationAttendance_Accomplished = September_submissions.aggregate(SchoolCelebrationAttendance_Accomplished=Sum('SchoolCelebrationAttendance_Accomplished'))['SchoolCelebrationAttendance_Accomplished']
    September_IPMT.TrainingAttendance_Accomplished = September_submissions.aggregate(TrainingAttendance_Accomplished=Sum('TrainingAttendance_Accomplished'))['TrainingAttendance_Accomplished']
    September_IPMT.FacultyMeetingAttendance_Accomplished = September_submissions.aggregate(FacultyMeetingAttendance_Accomplished=Sum('FacultyMeetingAttendance_Accomplished'))['FacultyMeetingAttendance_Accomplished']
    September_IPMT.AccreditationAttendance_Accomplished = September_submissions.aggregate(AccreditationAttendance_Accomplished=Sum('AccreditationAttendance_Accomplished'))['AccreditationAttendance_Accomplished']
    September_IPMT.SpiritualActivityAttendance_Accomplished = September_submissions.aggregate(SpiritualActivityAttendance_Accomplished=Sum('SpiritualActivityAttendance_Accomplished'))['SpiritualActivityAttendance_Accomplished']
    September_IPMT.author = request.user
    September_IPMT.IPCR_Submitted = datetime.now().date()
    
    October_submissions = IPMT_Form_model.objects.filter(
        Q(author=current_user),
        Q(IPCR_Saved__month=month_oct),
        Q(IPCR_Saved__year=current_year),
    )
    
    October_IPMT.syllabus_Accomplished = October_submissions.aggregate(syllabus_Accomplished=Sum('syllabus_Accomplished'))['syllabus_Accomplished']
    October_IPMT.CourseGuide_Accomplished = October_submissions.aggregate(CourseGuide_Accomplished=Sum('CourseGuide_Accomplished'))['CourseGuide_Accomplished']
    October_IPMT.SLM_Accomplished = October_submissions.aggregate(SLM_Accomplished=Sum('SLM_Accomplished'))['SLM_Accomplished']
    October_IPMT.SubjectAreas_Accomplished = October_submissions.aggregate(SubjectAreas_Accomplished=Sum('SubjectAreas_Accomplished'))['SubjectAreas_Accomplished']
    October_IPMT.AttendanceSheet_Accomplished = October_submissions.aggregate(AttendanceSheet_Accomplished=Sum('AttendanceSheet_Accomplished'))['AttendanceSheet_Accomplished']
    October_IPMT.ClassRecord_Accomplished = October_submissions.aggregate(ClassRecord_Accomplished=Sum('ClassRecord_Accomplished'))['ClassRecord_Accomplished']
    October_IPMT.TeachingEffectiveness_Accomplished = October_submissions.aggregate(TeachingEffectiveness_Accomplished=Sum('TeachingEffectiveness_Accomplished'))['TeachingEffectiveness_Accomplished']
    October_IPMT.ClassroomObservation_Accomplished = October_submissions.aggregate(ClassroomObservation_Accomplished=Sum('ClassroomObservation_Accomplished'))['ClassroomObservation_Accomplished']
    October_IPMT.TOSRubrics_Accomplished = October_submissions.aggregate(TOSRubrics_Accomplished=Sum('TOSRubrics_Accomplished'))['TOSRubrics_Accomplished']
    October_IPMT.TestQuestions_Accomplished = October_submissions.aggregate(TestQuestions_Accomplished=Sum('TestQuestions_Accomplished'))['TestQuestions_Accomplished']
    October_IPMT.AnswerKey_Accomplished = October_submissions.aggregate(AnswerKey_Accomplished=Sum('AnswerKey_Accomplished'))['AnswerKey_Accomplished']
    October_IPMT.GradingSheet_Accomplished = October_submissions.aggregate(GradingSheet_Accomplished=Sum('GradingSheet_Accomplished'))['GradingSheet_Accomplished']
    October_IPMT.StudentAdviced_Accomplished = October_submissions.aggregate(StudentAdviced_Accomplished=Sum('StudentAdviced_Accomplished'))['StudentAdviced_Accomplished']
    October_IPMT.AccomplishmentReport_Accomplished = October_submissions.aggregate(AccomplishmentReport_Accomplished=Sum('AccomplishmentReport_Accomplished'))['AccomplishmentReport_Accomplished']
    October_IPMT.ResearchProposalSubmitted_Accomplished = October_submissions.aggregate(ResearchProposalSubmitted_Accomplished=Sum('ResearchProposalSubmitted_Accomplished'))['ResearchProposalSubmitted_Accomplished']
    October_IPMT.ResearchImplemented_Accomplished = October_submissions.aggregate(ResearchImplemented_Accomplished=Sum('ResearchImplemented_Accomplished'))['ResearchImplemented_Accomplished']
    October_IPMT.ResearchPresented_Accomplished = October_submissions.aggregate(ResearchPresented_Accomplished=Sum('ResearchPresented_Accomplished'))['ResearchPresented_Accomplished']
    October_IPMT.ResearchPublished_Accomplished = October_submissions.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
    October_IPMT.ApprovedIPRights_Accomplished = October_submissions.aggregate(ApprovedIPRights_Accomplished=Sum('ApprovedIPRights_Accomplished'))['ApprovedIPRights_Accomplished']
    October_IPMT.ResearchUtilized_Accomplished = October_submissions.aggregate(ResearchUtilized_Accomplished=Sum('ResearchUtilized_Accomplished'))['ResearchUtilized_Accomplished']
    October_IPMT.NumberOfCitations_Accomplished = October_submissions.aggregate(NumberOfCitations_Accomplished=Sum('NumberOfCitations_Accomplished'))['NumberOfCitations_Accomplished']
    October_IPMT.ExtensionProposalSubmitted_Accomplished = October_submissions.aggregate(ExtensionProposalSubmitted_Accomplished=Sum('ExtensionProposalSubmitted_Accomplished'))['ExtensionProposalSubmitted_Accomplished']
    October_IPMT.PersonTrained_Accomplished = October_submissions.aggregate(PersonTrained_Accomplished=Sum('PersonTrained_Accomplished'))['PersonTrained_Accomplished']
    October_IPMT.PersonAvailedRatedGood_Accomplished = October_submissions.aggregate(PersonAvailedRatedGood_Accomplished=Sum('PersonAvailedRatedGood_Accomplished'))['PersonAvailedRatedGood_Accomplished']
    October_IPMT.PersonTrainedRatedGood_Accomplished = October_submissions.aggregate(PersonTrainedRatedGood_Accomplished=Sum('PersonTrainedRatedGood_Accomplished'))['PersonTrainedRatedGood_Accomplished']
    October_IPMT.TechnicalAdvice_Accomplished = October_submissions.aggregate(TechnicalAdvice_Accomplished=Sum('TechnicalAdvice_Accomplished'))['TechnicalAdvice_Accomplished']
    October_IPMT.AccomplishmentReportDeligatedAssignment_Accomplished = October_submissions.aggregate(AccomplishmentReportDeligatedAssignment_Accomplished=Sum('AccomplishmentReportDeligatedAssignment_Accomplished'))['AccomplishmentReportDeligatedAssignment_Accomplished']
    October_IPMT.FlagRaisingAttendance_Accomplished = October_submissions.aggregate(FlagRaisingAttendance_Accomplished=Sum('FlagRaisingAttendance_Accomplished'))['FlagRaisingAttendance_Accomplished']
    October_IPMT.FlagLoweringAttendance_Accomplished = October_submissions.aggregate(FlagLoweringAttendance_Accomplished=Sum('FlagLoweringAttendance_Accomplished'))['FlagLoweringAttendance_Accomplished']
    October_IPMT.WellnessProgramAttendance_Accomplished = October_submissions.aggregate(WellnessProgramAttendance_Accomplished=Sum('WellnessProgramAttendance_Accomplished'))['WellnessProgramAttendance_Accomplished']
    October_IPMT.SchoolCelebrationAttendance_Accomplished = October_submissions.aggregate(SchoolCelebrationAttendance_Accomplished=Sum('SchoolCelebrationAttendance_Accomplished'))['SchoolCelebrationAttendance_Accomplished']
    October_IPMT.TrainingAttendance_Accomplished = October_submissions.aggregate(TrainingAttendance_Accomplished=Sum('TrainingAttendance_Accomplished'))['TrainingAttendance_Accomplished']
    October_IPMT.FacultyMeetingAttendance_Accomplished = October_submissions.aggregate(FacultyMeetingAttendance_Accomplished=Sum('FacultyMeetingAttendance_Accomplished'))['FacultyMeetingAttendance_Accomplished']
    October_IPMT.AccreditationAttendance_Accomplished = October_submissions.aggregate(AccreditationAttendance_Accomplished=Sum('AccreditationAttendance_Accomplished'))['AccreditationAttendance_Accomplished']
    October_IPMT.SpiritualActivityAttendance_Accomplished = October_submissions.aggregate(SpiritualActivityAttendance_Accomplished=Sum('SpiritualActivityAttendance_Accomplished'))['SpiritualActivityAttendance_Accomplished']
    October_IPMT.author = request.user
    October_IPMT.IPCR_Submitted = datetime.now().date()
    
    November_submissions = IPMT_Form_model.objects.filter(
        Q(author=current_user),
        Q(IPCR_Saved__month=month_nov),
        Q(IPCR_Saved__year=current_year),
    )
    
    November_IPMT.syllabus_Accomplished = November_submissions.aggregate(syllabus_Accomplished=Sum('syllabus_Accomplished'))['syllabus_Accomplished']
    November_IPMT.CourseGuide_Accomplished = November_submissions.aggregate(CourseGuide_Accomplished=Sum('CourseGuide_Accomplished'))['CourseGuide_Accomplished']
    November_IPMT.SLM_Accomplished = November_submissions.aggregate(SLM_Accomplished=Sum('SLM_Accomplished'))['SLM_Accomplished']
    November_IPMT.SubjectAreas_Accomplished = November_submissions.aggregate(SubjectAreas_Accomplished=Sum('SubjectAreas_Accomplished'))['SubjectAreas_Accomplished']
    November_IPMT.AttendanceSheet_Accomplished = November_submissions.aggregate(AttendanceSheet_Accomplished=Sum('AttendanceSheet_Accomplished'))['AttendanceSheet_Accomplished']
    November_IPMT.ClassRecord_Accomplished = November_submissions.aggregate(ClassRecord_Accomplished=Sum('ClassRecord_Accomplished'))['ClassRecord_Accomplished']
    November_IPMT.TeachingEffectiveness_Accomplished = November_submissions.aggregate(TeachingEffectiveness_Accomplished=Sum('TeachingEffectiveness_Accomplished'))['TeachingEffectiveness_Accomplished']
    November_IPMT.ClassroomObservation_Accomplished = November_submissions.aggregate(ClassroomObservation_Accomplished=Sum('ClassroomObservation_Accomplished'))['ClassroomObservation_Accomplished']
    November_IPMT.TOSRubrics_Accomplished = November_submissions.aggregate(TOSRubrics_Accomplished=Sum('TOSRubrics_Accomplished'))['TOSRubrics_Accomplished']
    November_IPMT.TestQuestions_Accomplished = November_submissions.aggregate(TestQuestions_Accomplished=Sum('TestQuestions_Accomplished'))['TestQuestions_Accomplished']
    November_IPMT.AnswerKey_Accomplished = November_submissions.aggregate(AnswerKey_Accomplished=Sum('AnswerKey_Accomplished'))['AnswerKey_Accomplished']
    November_IPMT.GradingSheet_Accomplished = November_submissions.aggregate(GradingSheet_Accomplished=Sum('GradingSheet_Accomplished'))['GradingSheet_Accomplished']
    November_IPMT.StudentAdviced_Accomplished = November_submissions.aggregate(StudentAdviced_Accomplished=Sum('StudentAdviced_Accomplished'))['StudentAdviced_Accomplished']
    November_IPMT.AccomplishmentReport_Accomplished = November_submissions.aggregate(AccomplishmentReport_Accomplished=Sum('AccomplishmentReport_Accomplished'))['AccomplishmentReport_Accomplished']
    November_IPMT.ResearchProposalSubmitted_Accomplished = November_submissions.aggregate(ResearchProposalSubmitted_Accomplished=Sum('ResearchProposalSubmitted_Accomplished'))['ResearchProposalSubmitted_Accomplished']
    November_IPMT.ResearchImplemented_Accomplished = November_submissions.aggregate(ResearchImplemented_Accomplished=Sum('ResearchImplemented_Accomplished'))['ResearchImplemented_Accomplished']
    November_IPMT.ResearchPresented_Accomplished = November_submissions.aggregate(ResearchPresented_Accomplished=Sum('ResearchPresented_Accomplished'))['ResearchPresented_Accomplished']
    November_IPMT.ResearchPublished_Accomplished = November_submissions.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
    November_IPMT.ApprovedIPRights_Accomplished = November_submissions.aggregate(ApprovedIPRights_Accomplished=Sum('ApprovedIPRights_Accomplished'))['ApprovedIPRights_Accomplished']
    November_IPMT.ResearchUtilized_Accomplished = November_submissions.aggregate(ResearchUtilized_Accomplished=Sum('ResearchUtilized_Accomplished'))['ResearchUtilized_Accomplished']
    November_IPMT.NumberOfCitations_Accomplished = November_submissions.aggregate(NumberOfCitations_Accomplished=Sum('NumberOfCitations_Accomplished'))['NumberOfCitations_Accomplished']
    November_IPMT.ExtensionProposalSubmitted_Accomplished = November_submissions.aggregate(ExtensionProposalSubmitted_Accomplished=Sum('ExtensionProposalSubmitted_Accomplished'))['ExtensionProposalSubmitted_Accomplished']
    November_IPMT.PersonTrained_Accomplished = November_submissions.aggregate(PersonTrained_Accomplished=Sum('PersonTrained_Accomplished'))['PersonTrained_Accomplished']
    November_IPMT.PersonAvailedRatedGood_Accomplished = November_submissions.aggregate(PersonAvailedRatedGood_Accomplished=Sum('PersonAvailedRatedGood_Accomplished'))['PersonAvailedRatedGood_Accomplished']
    November_IPMT.PersonTrainedRatedGood_Accomplished = November_submissions.aggregate(PersonTrainedRatedGood_Accomplished=Sum('PersonTrainedRatedGood_Accomplished'))['PersonTrainedRatedGood_Accomplished']
    November_IPMT.TechnicalAdvice_Accomplished = November_submissions.aggregate(TechnicalAdvice_Accomplished=Sum('TechnicalAdvice_Accomplished'))['TechnicalAdvice_Accomplished']
    November_IPMT.AccomplishmentReportDeligatedAssignment_Accomplished = November_submissions.aggregate(AccomplishmentReportDeligatedAssignment_Accomplished=Sum('AccomplishmentReportDeligatedAssignment_Accomplished'))['AccomplishmentReportDeligatedAssignment_Accomplished']
    November_IPMT.FlagRaisingAttendance_Accomplished = November_submissions.aggregate(FlagRaisingAttendance_Accomplished=Sum('FlagRaisingAttendance_Accomplished'))['FlagRaisingAttendance_Accomplished']
    November_IPMT.FlagLoweringAttendance_Accomplished = November_submissions.aggregate(FlagLoweringAttendance_Accomplished=Sum('FlagLoweringAttendance_Accomplished'))['FlagLoweringAttendance_Accomplished']
    November_IPMT.WellnessProgramAttendance_Accomplished = November_submissions.aggregate(WellnessProgramAttendance_Accomplished=Sum('WellnessProgramAttendance_Accomplished'))['WellnessProgramAttendance_Accomplished']
    November_IPMT.SchoolCelebrationAttendance_Accomplished = November_submissions.aggregate(SchoolCelebrationAttendance_Accomplished=Sum('SchoolCelebrationAttendance_Accomplished'))['SchoolCelebrationAttendance_Accomplished']
    November_IPMT.TrainingAttendance_Accomplished = November_submissions.aggregate(TrainingAttendance_Accomplished=Sum('TrainingAttendance_Accomplished'))['TrainingAttendance_Accomplished']
    November_IPMT.FacultyMeetingAttendance_Accomplished = November_submissions.aggregate(FacultyMeetingAttendance_Accomplished=Sum('FacultyMeetingAttendance_Accomplished'))['FacultyMeetingAttendance_Accomplished']
    November_IPMT.AccreditationAttendance_Accomplished = November_submissions.aggregate(AccreditationAttendance_Accomplished=Sum('AccreditationAttendance_Accomplished'))['AccreditationAttendance_Accomplished']
    November_IPMT.SpiritualActivityAttendance_Accomplished = November_submissions.aggregate(SpiritualActivityAttendance_Accomplished=Sum('SpiritualActivityAttendance_Accomplished'))['SpiritualActivityAttendance_Accomplished']
    November_IPMT.author = request.user
    November_IPMT.IPCR_Submitted = datetime.now().date()
    
    December_submissions = IPMT_Form_model.objects.filter(
        Q(author=current_user),
        Q(IPCR_Saved__month=month_dec),
        Q(IPCR_Saved__year=current_year),
    )
    
    December_IPMT.syllabus_Accomplished = December_submissions.aggregate(syllabus_Accomplished=Sum('syllabus_Accomplished'))['syllabus_Accomplished']
    December_IPMT.CourseGuide_Accomplished = December_submissions.aggregate(CourseGuide_Accomplished=Sum('CourseGuide_Accomplished'))['CourseGuide_Accomplished']
    December_IPMT.SLM_Accomplished = December_submissions.aggregate(SLM_Accomplished=Sum('SLM_Accomplished'))['SLM_Accomplished']
    December_IPMT.SubjectAreas_Accomplished = December_submissions.aggregate(SubjectAreas_Accomplished=Sum('SubjectAreas_Accomplished'))['SubjectAreas_Accomplished']
    December_IPMT.AttendanceSheet_Accomplished = December_submissions.aggregate(AttendanceSheet_Accomplished=Sum('AttendanceSheet_Accomplished'))['AttendanceSheet_Accomplished']
    December_IPMT.ClassRecord_Accomplished = December_submissions.aggregate(ClassRecord_Accomplished=Sum('ClassRecord_Accomplished'))['ClassRecord_Accomplished']
    December_IPMT.TeachingEffectiveness_Accomplished = December_submissions.aggregate(TeachingEffectiveness_Accomplished=Sum('TeachingEffectiveness_Accomplished'))['TeachingEffectiveness_Accomplished']
    December_IPMT.ClassroomObservation_Accomplished = December_submissions.aggregate(ClassroomObservation_Accomplished=Sum('ClassroomObservation_Accomplished'))['ClassroomObservation_Accomplished']
    December_IPMT.TOSRubrics_Accomplished = December_submissions.aggregate(TOSRubrics_Accomplished=Sum('TOSRubrics_Accomplished'))['TOSRubrics_Accomplished']
    December_IPMT.TestQuestions_Accomplished = December_submissions.aggregate(TestQuestions_Accomplished=Sum('TestQuestions_Accomplished'))['TestQuestions_Accomplished']
    December_IPMT.AnswerKey_Accomplished = December_submissions.aggregate(AnswerKey_Accomplished=Sum('AnswerKey_Accomplished'))['AnswerKey_Accomplished']
    December_IPMT.GradingSheet_Accomplished = December_submissions.aggregate(GradingSheet_Accomplished=Sum('GradingSheet_Accomplished'))['GradingSheet_Accomplished']
    December_IPMT.StudentAdviced_Accomplished = December_submissions.aggregate(StudentAdviced_Accomplished=Sum('StudentAdviced_Accomplished'))['StudentAdviced_Accomplished']
    December_IPMT.AccomplishmentReport_Accomplished = December_submissions.aggregate(AccomplishmentReport_Accomplished=Sum('AccomplishmentReport_Accomplished'))['AccomplishmentReport_Accomplished']
    December_IPMT.ResearchProposalSubmitted_Accomplished = December_submissions.aggregate(ResearchProposalSubmitted_Accomplished=Sum('ResearchProposalSubmitted_Accomplished'))['ResearchProposalSubmitted_Accomplished']
    December_IPMT.ResearchImplemented_Accomplished = December_submissions.aggregate(ResearchImplemented_Accomplished=Sum('ResearchImplemented_Accomplished'))['ResearchImplemented_Accomplished']
    December_IPMT.ResearchPresented_Accomplished = December_submissions.aggregate(ResearchPresented_Accomplished=Sum('ResearchPresented_Accomplished'))['ResearchPresented_Accomplished']
    December_IPMT.ResearchPublished_Accomplished = December_submissions.aggregate(ResearchPublished_Accomplished=Sum('ResearchPublished_Accomplished'))['ResearchPublished_Accomplished']
    December_IPMT.ApprovedIPRights_Accomplished = December_submissions.aggregate(ApprovedIPRights_Accomplished=Sum('ApprovedIPRights_Accomplished'))['ApprovedIPRights_Accomplished']
    December_IPMT.ResearchUtilized_Accomplished = December_submissions.aggregate(ResearchUtilized_Accomplished=Sum('ResearchUtilized_Accomplished'))['ResearchUtilized_Accomplished']
    December_IPMT.NumberOfCitations_Accomplished = December_submissions.aggregate(NumberOfCitations_Accomplished=Sum('NumberOfCitations_Accomplished'))['NumberOfCitations_Accomplished']
    December_IPMT.ExtensionProposalSubmitted_Accomplished = December_submissions.aggregate(ExtensionProposalSubmitted_Accomplished=Sum('ExtensionProposalSubmitted_Accomplished'))['ExtensionProposalSubmitted_Accomplished']
    December_IPMT.PersonTrained_Accomplished = December_submissions.aggregate(PersonTrained_Accomplished=Sum('PersonTrained_Accomplished'))['PersonTrained_Accomplished']
    December_IPMT.PersonAvailedRatedGood_Accomplished = December_submissions.aggregate(PersonAvailedRatedGood_Accomplished=Sum('PersonAvailedRatedGood_Accomplished'))['PersonAvailedRatedGood_Accomplished']
    December_IPMT.PersonTrainedRatedGood_Accomplished = December_submissions.aggregate(PersonTrainedRatedGood_Accomplished=Sum('PersonTrainedRatedGood_Accomplished'))['PersonTrainedRatedGood_Accomplished']
    December_IPMT.TechnicalAdvice_Accomplished = December_submissions.aggregate(TechnicalAdvice_Accomplished=Sum('TechnicalAdvice_Accomplished'))['TechnicalAdvice_Accomplished']
    December_IPMT.AccomplishmentReportDeligatedAssignment_Accomplished = December_submissions.aggregate(AccomplishmentReportDeligatedAssignment_Accomplished=Sum('AccomplishmentReportDeligatedAssignment_Accomplished'))['AccomplishmentReportDeligatedAssignment_Accomplished']
    December_IPMT.FlagRaisingAttendance_Accomplished = December_submissions.aggregate(FlagRaisingAttendance_Accomplished=Sum('FlagRaisingAttendance_Accomplished'))['FlagRaisingAttendance_Accomplished']
    December_IPMT.FlagLoweringAttendance_Accomplished = December_submissions.aggregate(FlagLoweringAttendance_Accomplished=Sum('FlagLoweringAttendance_Accomplished'))['FlagLoweringAttendance_Accomplished']
    December_IPMT.WellnessProgramAttendance_Accomplished = December_submissions.aggregate(WellnessProgramAttendance_Accomplished=Sum('WellnessProgramAttendance_Accomplished'))['WellnessProgramAttendance_Accomplished']
    December_IPMT.SchoolCelebrationAttendance_Accomplished = December_submissions.aggregate(SchoolCelebrationAttendance_Accomplished=Sum('SchoolCelebrationAttendance_Accomplished'))['SchoolCelebrationAttendance_Accomplished']
    December_IPMT.TrainingAttendance_Accomplished = December_submissions.aggregate(TrainingAttendance_Accomplished=Sum('TrainingAttendance_Accomplished'))['TrainingAttendance_Accomplished']
    December_IPMT.FacultyMeetingAttendance_Accomplished = December_submissions.aggregate(FacultyMeetingAttendance_Accomplished=Sum('FacultyMeetingAttendance_Accomplished'))['FacultyMeetingAttendance_Accomplished']
    December_IPMT.AccreditationAttendance_Accomplished = December_submissions.aggregate(AccreditationAttendance_Accomplished=Sum('AccreditationAttendance_Accomplished'))['AccreditationAttendance_Accomplished']
    December_IPMT.SpiritualActivityAttendance_Accomplished = December_submissions.aggregate(SpiritualActivityAttendance_Accomplished=Sum('SpiritualActivityAttendance_Accomplished'))['SpiritualActivityAttendance_Accomplished']
    December_IPMT.author = request.user
    December_IPMT.IPCR_Submitted = datetime.now().date()
    
    if('no' in request.POST):
        return redirect('IPCR_Form')
    
    else:
        new_instance.save()
        January_IPMT.save()
        February_IPMT.save()
        March_IPMT.save()
        April_IPMT.save()
        May_IPMT.save()
        June_IPMT.save()
        July_IPMT.save()
        August_IPMT.save()
        September_IPMT.save()
        October_IPMT.save()
        November_IPMT.save()
        December_IPMT.save()
        messages.success(request, "You've successfully submitted your IPCR form.")
        
        if new_instance.syllabus_Accomplished >= new_instance.syllabus_Target:
            Remarks_IPMT.Remarks_syllabus_Accomplished = "Met"
        
        elif new_instance.syllabus_Accomplished < new_instance.syllabus_Target:
            Remarks_IPMT.Remarks_syllabus_Accomplished = "Unmet"
            
        if new_instance.CourseGuide_Accomplished >= new_instance.CourseGuide_Target:
            Remarks_IPMT.Remarks_CourseGuide_Accomplished = "Met"
        
        elif new_instance.CourseGuide_Accomplished < new_instance.CourseGuide_Target:
            Remarks_IPMT.Remarks_CourseGuide_Accomplished = "Unmet"
            
        if new_instance.SLM_Accomplished >= new_instance.SLM_Target:
            Remarks_IPMT.Remarks_SLM_Accomplished = "Met"
        
        elif new_instance.SLM_Accomplished < new_instance.SLM_Target:
            Remarks_IPMT.Remarks_SLM_Accomplished = "Unmet"
            
        if new_instance.SubjectAreas_Accomplished >= new_instance.SubjectAreas_Target:
            Remarks_IPMT.Remarks_SubjectAreas_Accomplished = "Met"
        
        elif new_instance.SubjectAreas_Accomplished < new_instance.SubjectAreas_Target:
            Remarks_IPMT.Remarks_SubjectAreas_Accomplished = "Unmet"
            
        if new_instance.AttendanceSheet_Accomplished >= new_instance.AttendanceSheet_Target:
            Remarks_IPMT.Remarks_AttendanceSheet_Accomplished = "Met"
        
        elif new_instance.AttendanceSheet_Accomplished < new_instance.AttendanceSheet_Target:
            Remarks_IPMT.Remarks_AttendanceSheet_Accomplished = "Unmet"
            
        if new_instance.ClassRecord_Accomplished >= new_instance.ClassRecord_Target:
            Remarks_IPMT.Remarks_ClassRecord_Accomplished = "Met"
        
        elif new_instance.ClassRecord_Accomplished < new_instance.ClassRecord_Target:
            Remarks_IPMT.Remarks_ClassRecord_Accomplished = "Unmet"
            
        if new_instance.TeachingEffectiveness_Accomplished >= new_instance.TeachingEffectiveness_Target:
            Remarks_IPMT.Remarks_TeachingEffectiveness_Accomplished = "Met"
        
        elif new_instance.TeachingEffectiveness_Accomplished < new_instance.TeachingEffectiveness_Target:
            Remarks_IPMT.Remarks_TeachingEffectiveness_Accomplished = "Unmet"
            
        if new_instance.ClassroomObservation_Accomplished >= new_instance.ClassroomObservation_Target:
            Remarks_IPMT.Remarks_ClassroomObservation_Accomplished = "Met"
        
        elif new_instance.ClassroomObservation_Accomplished < new_instance.ClassroomObservation_Target:
            Remarks_IPMT.Remarks_ClassroomObservation_Accomplished = "Unmet"
            
        if (new_instance.MidtermTOSRubrics_Accomplished + new_instance.FinaltermTOSRubrics_Accomplished) >= (new_instance.MidtermTOSRubrics_Target + new_instance.FinaltermTOSRubrics_Target):
            Remarks_IPMT.Remarks_TOSRubrics_Accomplished = "Met"
        
        elif (new_instance.MidtermTOSRubrics_Accomplished + new_instance.FinaltermTOSRubrics_Accomplished) < (new_instance.MidtermTOSRubrics_Target + new_instance.FinaltermTOSRubrics_Target):
            Remarks_IPMT.Remarks_TOSRubrics_Accomplished = "Unmet"
        
        if (new_instance.MidtermTestQuestions_Accomplished + new_instance.FinaltermTestQuestions_Accomplished) >= (new_instance.MidtermTestQuestions_Target + new_instance.FinaltermTestQuestions_Target):
            Remarks_IPMT.Remarks_TestQuestions_Accomplished = "Met"
        
        elif (new_instance.MidtermTestQuestions_Accomplished + new_instance.FinaltermTestQuestions_Accomplished) < (new_instance.MidtermTestQuestions_Target + new_instance.FinaltermTestQuestions_Target):
            Remarks_IPMT.Remarks_TestQuestions_Accomplished = "Unmet"
            
        if (new_instance.MidtermAnswerKey_Accomplished + new_instance.FinaltermAnswerKey_Accomplished) >= (new_instance.MidtermAnswerKey_Target + new_instance.FinaltermAnswerKey_Target):
            Remarks_IPMT.Remarks_AnswerKey_Accomplished = "Met"
        
        elif (new_instance.MidtermAnswerKey_Accomplished + new_instance.FinaltermAnswerKey_Accomplished) < (new_instance.MidtermAnswerKey_Target + new_instance.FinaltermAnswerKey_Target):
            Remarks_IPMT.Remarks_AnswerKey_Accomplished = "Unmet"
            
        if new_instance.GradingSheet_Accomplished >= new_instance.GradingSheet_Target:
            Remarks_IPMT.Remarks_GradingSheet_Accomplished = "Met"
        
        elif new_instance.GradingSheet_Accomplished < new_instance.GradingSheet_Target:
            Remarks_IPMT.Remarks_GradingSheet_Accomplished = "Unmet"
            
        if new_instance.StudentAdviced_Accomplished >= new_instance.StudentAdviced_Target:
            Remarks_IPMT.Remarks_StudentAdviced_Accomplished = "Met"
        
        elif new_instance.StudentAdviced_Accomplished < new_instance.StudentAdviced_Target:
            Remarks_IPMT.Remarks_StudentAdviced_Accomplished = "Unmet"
        
        if new_instance.AccomplishmentReport_Accomplished >= new_instance.AccomplishmentReport_Target:
            Remarks_IPMT.Remarks_AccomplishmentReport_Accomplished = "Met"
        
        elif new_instance.AccomplishmentReport_Accomplished < new_instance.AccomplishmentReport_Target:
            Remarks_IPMT.Remarks_AccomplishmentReport_Accomplished = "Unmet"
            
        if new_instance.ResearchProposalSubmitted_Accomplished >= new_instance.ResearchProposalSubmitted_Target:
            Remarks_IPMT.Remarks_ResearchProposalSubmitted_Accomplished = "Met"
        
        elif new_instance.ResearchProposalSubmitted_Accomplished < new_instance.ResearchProposalSubmitted_Target:
            Remarks_IPMT.Remarks_ResearchProposalSubmitted_Accomplished = "Unmet"
        
        if new_instance.ResearchImplemented_Accomplished >= new_instance.ResearchImplemented_Target:
            Remarks_IPMT.Remarks_ResearchImplemented_Accomplished = "Met"
        
        elif new_instance.ResearchImplemented_Accomplished < new_instance.ResearchImplemented_Target:
            Remarks_IPMT.Remarks_ResearchImplemented_Accomplished = "Unmet"
            
        if new_instance.ResearchPresented_Accomplished >= new_instance.ResearchPresented_Target:
            Remarks_IPMT.Remarks_ResearchPresented_Accomplished = "Met"
        
        elif new_instance.ResearchPresented_Accomplished < new_instance.ResearchPresented_Target:
            Remarks_IPMT.Remarks_ResearchPresented_Accomplished = "Unmet"
            
        if new_instance.ResearchPublished_Accomplished >= new_instance.ResearchPublished_Target:
            Remarks_IPMT.Remarks_ResearchPublished_Accomplished = "Met"
        
        elif new_instance.ResearchPublished_Accomplished < new_instance.ResearchPublished_Target:
            Remarks_IPMT.Remarks_ResearchPublished_Accomplished = "Unmet"
            
        if new_instance.ApprovedIPRights_Accomplished >= new_instance.ApprovedIPRights_Target:
            Remarks_IPMT.Remarks_ApprovedIPRights_Accomplished = "Met"
        
        elif new_instance.ApprovedIPRights_Accomplished < new_instance.ApprovedIPRights_Target:
            Remarks_IPMT.Remarks_ApprovedIPRights_Accomplished = "Unmet"
            
        if new_instance.ResearchUtilized_Accomplished >= new_instance.ResearchUtilized_Target:
            Remarks_IPMT.Remarks_ResearchUtilized_Accomplished = "Met"
        
        elif new_instance.ResearchUtilized_Accomplished < new_instance.ResearchUtilized_Target:
            Remarks_IPMT.Remarks_ResearchUtilized_Accomplished = "Unmet"
            
        if new_instance.NumberOfCitations_Accomplished >= new_instance.NumberOfCitations_Target:
            Remarks_IPMT.Remarks_NumberOfCitations_Accomplished = "Met"
        
        elif new_instance.NumberOfCitations_Accomplished < new_instance.NumberOfCitations_Target:
            Remarks_IPMT.Remarks_NumberOfCitations_Accomplished = "Unmet"
            
        if new_instance.ExtensionProposalSubmitted_Accomplished >= new_instance.ExtensionProposalSubmitted_Target:
            Remarks_IPMT.Remarks_ExtensionProposalSubmitted_Accomplished = "Met"
        
        elif new_instance.ExtensionProposalSubmitted_Accomplished < new_instance.ExtensionProposalSubmitted_Target:
            Remarks_IPMT.Remarks_ExtensionProposalSubmitted_Accomplished = "Unmet"
            
        if new_instance.PersonTrained_Accomplished >= new_instance.PersonTrained_Target:
            Remarks_IPMT.Remarks_PersonTrained_Accomplished = "Met"
        
        elif new_instance.PersonTrained_Accomplished < new_instance.PersonTrained_Target:
            Remarks_IPMT.Remarks_PersonTrained_Accomplished = "Unmet"
            
        if new_instance.PersonAvailedRatedGood_Accomplished >= new_instance.PersonAvailedRatedGood_Target:
            Remarks_IPMT.Remarks_PersonAvailedRatedGood_Accomplished = "Met"
        
        elif new_instance.PersonAvailedRatedGood_Accomplished < new_instance.PersonAvailedRatedGood_Target:
            Remarks_IPMT.Remarks_PersonAvailedRatedGood_Accomplished = "Unmet"
            
        if new_instance.PersonTrainedRatedGood_Accomplished >= new_instance.PersonTrainedRatedGood_Target:
            Remarks_IPMT.Remarks_PersonTrainedRatedGood_Accomplished = "Met"
        
        elif new_instance.PersonTrainedRatedGood_Accomplished < new_instance.PersonTrainedRatedGood_Target:
            Remarks_IPMT.Remarks_PersonTrainedRatedGood_Accomplished = "Unmet"
            
        if new_instance.TechnicalAdvice_Accomplished >= new_instance.TechnicalAdvice_Target:
            Remarks_IPMT.Remarks_TechnicalAdvice_Accomplished = "Met"
        
        elif new_instance.TechnicalAdvice_Accomplished < new_instance.TechnicalAdvice_Target:
            Remarks_IPMT.Remarks_TechnicalAdvice_Accomplished = "Unmet"
            
        if new_instance.AccomplishmentReportDeligatedAssignment_Accomplished >= new_instance.AccomplishmentReportDeligatedAssignment_Target:
            Remarks_IPMT.Remarks_AccomplishmentReportDeligatedAssignment_Accomplished = "Met"
        
        elif new_instance.AccomplishmentReportDeligatedAssignment_Accomplished < new_instance.AccomplishmentReportDeligatedAssignment_Target:
            Remarks_IPMT.Remarks_AccomplishmentReportDeligatedAssignment_Accomplished = "Unmet"
            
        if new_instance.FlagRaisingAttendance_Accomplished >= new_instance.FlagRaisingAttendance_Target:
            Remarks_IPMT.Remarks_FlagRaisingAttendance_Accomplished = "Met"
        
        elif new_instance.FlagRaisingAttendance_Accomplished < new_instance.FlagRaisingAttendance_Target:
            Remarks_IPMT.Remarks_FlagRaisingAttendance_Accomplished = "Unmet"
            
        if new_instance.FlagLoweringAttendance_Accomplished >= new_instance.FlagLoweringAttendance_Target:
            Remarks_IPMT.Remarks_FlagLoweringAttendance_Accomplished = "Met"
        
        elif new_instance.FlagLoweringAttendance_Accomplished < new_instance.FlagLoweringAttendance_Target:
            Remarks_IPMT.Remarks_FlagLoweringAttendance_Accomplished = "Unmet"
            
        if new_instance.WellnessProgramAttendance_Accomplished >= new_instance.WellnessProgramAttendance_Target:
            Remarks_IPMT.Remarks_WellnessProgramAttendance_Accomplished = "Met"
        
        elif new_instance.WellnessProgramAttendance_Accomplished < new_instance.WellnessProgramAttendance_Target:
            Remarks_IPMT.Remarks_WellnessProgramAttendance_Accomplished = "Unmet"
            
        if new_instance.SchoolCelebrationAttendance_Accomplished >= new_instance.SchoolCelebrationAttendance_Target:
            Remarks_IPMT.Remarks_SchoolCelebrationAttendance_Accomplished = "Met"
        
        elif new_instance.SchoolCelebrationAttendance_Accomplished < new_instance.SchoolCelebrationAttendance_Target:
            Remarks_IPMT.Remarks_SchoolCelebrationAttendance_Accomplished = "Unmet"
            
        if new_instance.TrainingAttendance_Accomplished >= new_instance.TrainingAttendance_Target:
            Remarks_IPMT.Remarks_TrainingAttendance_Accomplished = "Met"
        
        elif new_instance.TrainingAttendance_Accomplished < new_instance.TrainingAttendance_Target:
            Remarks_IPMT.Remarks_TrainingAttendance_Accomplished = "Unmet"
            
        if new_instance.FacultyMeetingAttendance_Accomplished >= new_instance.FacultyMeetingAttendance_Target:
            Remarks_IPMT.Remarks_FacultyMeetingAttendance_Accomplished = "Met"
        
        elif new_instance.FacultyMeetingAttendance_Accomplished < new_instance.FacultyMeetingAttendance_Target:
            Remarks_IPMT.Remarks_FacultyMeetingAttendance_Accomplished = "Unmet"
            
        if new_instance.AccreditationAttendance_Accomplished >= new_instance.AccreditationAttendance_Target:
            Remarks_IPMT.Remarks_AccreditationAttendance_Accomplished = "Met"
        
        elif new_instance.AccreditationAttendance_Accomplished < new_instance.AccreditationAttendance_Target:
            Remarks_IPMT.Remarks_AccreditationAttendance_Accomplished = "Unmet"
            
        if new_instance.SpiritualActivityAttendance_Accomplished >= new_instance.SpiritualActivityAttendance_Target:
            Remarks_IPMT.Remarks_SpiritualActivityAttendance_Accomplished = "Met"
        
        elif new_instance.SpiritualActivityAttendance_Accomplished < new_instance.SpiritualActivityAttendance_Target:
            Remarks_IPMT.Remarks_SpiritualActivityAttendance_Accomplished = "Unmet"
        
        Remarks_IPMT.author = request.user
        Remarks_IPMT.IPMT_Submitted = datetime.now().date()
        Remarks_IPMT.save()
        return redirect('IPCR_Form')

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Member'])  
def IPCR_Form_Already_Submitted(request):
    return render(request, 'forms/IPCRForm_AlreadySubmitted.html')