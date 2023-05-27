from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date, datetime
from django.forms import modelform_factory
from django.db.models import Sum

# Create your views here.

def IPCR_Form(request):
    IPCRForm = modelform_factory(IPCR_Form_model, fields="__all__", exclude= ['author', 'department', 'IPCR_Submitted', 'IPCR_Deadline'])

    # Check if the user already has a saved instance of IPCR_Form_model
    try:
        existing_instance = IPCR_Form_model.objects.get(author=request.user)
    except IPCR_Form_model.DoesNotExist:
        existing_instance = None

    if request.method == 'POST':
        forms = IPCRForm(request.POST, instance=existing_instance)
        if forms.is_valid():
            current_user = request.user
            group_names = [group.name for group in current_user.groups.all()]
            model_instance = forms.save(commit=False)
            model_instance.author = current_user
            model_instance.department = ', '.join(group_names)
            current_date = datetime.now().date()
            deadline_date = datetime.strptime("2023-06-16", "%Y-%m-%d").date()
                
            if current_date <= deadline_date:
                model_instance.IPCR_Deadline = date(2023, 6, 16)
                model_instance.save()
                
            model_instance.save()
            
            if IPMT_Form_model.objects.filter(author = request.user).exists() == False:
                source_instance = IPCR_Form_model.objects.get(author = request.user)
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
            
            else:
                print("Else")
                past_instance = IPMT_Form_model.objects.filter(author = request.user)
                total_IPCR = past_instance.aggregate(
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
                
                source_instance = IPCR_Form_model.objects.get(author = request.user)
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
            return redirect('IPCR_Form')

    else:
        forms = IPCRForm(instance=existing_instance)

    context = {
        'forms': forms
    }
    return render(request, 'forms/IPCRForm_Submit.html', context)

