from django.shortcuts import render, redirect
from forms.forms import *
from forms.models import *
from django.contrib.auth.models import User, Group

# Create your views here.
def member_faculty_list(request):
    return render(request, ('faculty_list/member_faculty_list.html'))


def admin_faculty_list(request, username):
    selected_author = None
    latest_submission = None

    if username:
        selected_author = User.objects.filter(username=username).first()
        if selected_author:
            latest_submission = IPCR_Submit_model.objects.filter(author=selected_author).latest('id')

    if latest_submission is None:
        initial_data = {
            'Syllabus_Remarks': '',
            'CourseGuide_Remarks': '',
            'SLM_Remarks': '',
            'SubjectAreas_Remarks' : '',
            'AttendanceSheet_Remarks': '',
            'ClassRecord_Remarks': '',
            'TeachingEffectiveness_Remarks': '',
            'ClassroomObservation_Remarks': '',
            'MidtermTOSRubrics_Remarks': '',
            'FinaltermTOSRubrics_Remarks': '',
            'MidtermTestQuestions_Remarks': '',
            'FinaltermTestQuestions_Remarks': '',
            'MidtermAnswerKey_Remarks': '',
            'FinaltermAnswerKey_Remarks': '',
            'GradingSheet_Remarks': '',
            'StudentAdviced_Remarks': '',
            'AccomplishmentReport_Remarks': '',
            'ResearchProposalSubmitted_Remarks': '',
            'ResearchImplemented_Remarks': '',
            'ResearchPresented_Remarks': '',
            'ResearchPublished_Remarks': '',
            'ApprovedIPRights_Remarks': '',
            'ResearchUtilized_Remarks': '',
            'NumberOfCitations_Remarks': '',
            'ExtensionProposalSubmitted_Remarks': '',
            'PersonTrained_Remarks': '',
            'PersonAvailedRatedGood_Remarks': '',
            'PersonTrainedRatedGood_Remarks': '',
            'TechnicalAdvice_Remarks': '',
            'AccomplishmentReportDeligatedAssignment_Remarks': '',
            'FlagRaisingAttendance_Remarks': '',
            'FlagLoweringAttendance_Remarks': '',
            'WellnessProgramAttendance_Remarks': '',
            'SchoolCelebrationAttendance_Remarks': '',
            'TrainingAttendance_Remarks': '',
            'FacultyMeetingAttendance_Remarks': '',
            'AccreditationAttendance_Remarks': '',
            'SpiritualActivityAttendance_Remarks': '',
        }
        
    else:
        initial_data = {
            'Syllabus_Remarks': latest_submission.syllabus_Remarks,
            'CourseGuide_Remarks': latest_submission.CourseGuide_Remarks,
            'SLM_Remarks': latest_submission.SLM_Remarks,
            'SubjectAreas_Remarks': latest_submission.SubjectAreas_Remarks, 
            'AttendanceSheet_Remarks': latest_submission.AttendanceSheet_Remarks,
            'ClassRecord_Remarks': latest_submission.ClassRecord_Remarks,
            'TeachingEffectiveness_Remarks': latest_submission.TeachingEffectiveness_Remarks,
            'ClassroomObservation_Remarks': latest_submission.ClassroomObservation_Remarks,
            'MidtermTOSRubrics_Remarks': latest_submission.MidtermTOSRubrics_Remarks,
            'FinaltermTOSRubrics_Remarks': latest_submission.FinaltermTOSRubrics_Remarks,
            'MidtermTestQuestions_Remarks': latest_submission.MidtermTestQuestions_Remarks,
            'FinaltermTestQuestions_Remarks': latest_submission.FinaltermTestQuestions_Remarks,
            'MidtermAnswerKey_Remarks': latest_submission.MidtermAnswerKey_Remarks,
            'FinaltermAnswerKey_Remarks': latest_submission.FinaltermAnswerKey_Remarks,
            'GradingSheet_Remarks': latest_submission.GradingSheet_Remarks,
            'StudentAdviced_Remarks': latest_submission.StudentAdviced_Remarks,
            'AccomplishmentReport_Remarks': latest_submission.AccomplishmentReport_Remarks,
            'ResearchProposalSubmitted_Remarks': latest_submission.ResearchProposalSubmitted_Remarks,
            'ResearchImplemented_Remarks': latest_submission.ResearchImplemented_Remarks,
            'ResearchPresented_Remarks': latest_submission.ResearchPresented_Remarks,
            'ResearchPublished_Remarks': latest_submission.ResearchPublished_Remarks,
            'ApprovedIPRights_Remarks': latest_submission.ApprovedIPRights_Remarks,
            'ResearchUtilized_Remarks': latest_submission.ResearchUtilized_Remarks,
            'NumberOfCitations_Remarks': latest_submission.NumberOfCitations_Remarks,
            'ExtensionProposalSubmitted_Remarks': latest_submission.ExtensionProposalSubmitted_Remarks,
            'PersonTrained_Remarks': latest_submission.PersonTrained_Remarks,
            'PersonAvailedRatedGood_Remarks': latest_submission.PersonAvailedRatedGood_Remarks,
            'PersonTrainedRatedGood_Remarks': latest_submission.PersonTrainedRatedGood_Remarks,
            'TechnicalAdvice_Remarks': latest_submission.TechnicalAdvice_Remarks,
            'AccomplishmentReportDeligatedAssignment_Remarks': latest_submission.AccomplishmentReportDeligatedAssignment_Remarks,
            'FlagRaisingAttendance_Remarks': latest_submission.FlagRaisingAttendance_Remarks,
            'FlagLoweringAttendance_Remarks': latest_submission.FlagLoweringAttendance_Remarks,
            'WellnessProgramAttendance_Remarks': latest_submission.WellnessProgramAttendance_Remarks,
            'SchoolCelebrationAttendance_Remarks': latest_submission.SchoolCelebrationAttendance_Remarks,
            'TrainingAttendance_Remarks': latest_submission.TrainingAttendance_Remarks,
            'FacultyMeetingAttendance_Remarks': latest_submission.FacultyMeetingAttendance_Remarks,
            'AccreditationAttendance_Remarks': latest_submission.AccreditationAttendance_Remarks,
            'SpiritualActivityAttendance_Remarks': latest_submission.SpiritualActivityAttendance_Remarks,       
        }      
                      
    if request.method == 'POST':
        form_syllabus = IPCR_Syllabus_form(request.POST, prefix="form_syllabus")
        form_courseguide = IPCR_CourseGuide_form(request.POST, prefix="form_courseguide")
        form_SLM = IPCR_SLM_form(request.POST, prefix="form_SLM")
        form_subjectareas = IPCR_SubjectAreas_form(request.POST, prefix = "form_subjectareas") 
        form_attendancesheet = IPCR_AttendanceSheet_form(request.POST, prefix = "form_attendancesheet")              
        form_classrecord = IPCR_ClassRecord_form(request.POST, prefix = "form_classrecord")              
        form_teachingeffectiveness = IPCR_TeachingEffectiveness_form(request.POST, prefix = "form_teachingeffectiveness")   
        form_classroomobservation = IPCR_ClassroomObservation_form(request.POST, prefix = "form_classroomobservation")   
        form_midtermtosrubrics = IPCR_MidtermTOSRubrics_form(request.POST, prefix = "form_midtermtosrubrics")   
        form_finaltermtosrubrics = IPCR_FinaltermTOSRubrics_form(request.POST, prefix = "form_finaltermtosrubrics")   
        form_midtermtestquestions = IPCR_MidtermTestQuestions_form(request.POST, prefix = "midtermtestquestions")   
        form_finaltermtestquestions = IPCR_FinaltermTestQuestions_form(request.POST, prefix = "finaltermtestquestions")   
        form_midtermanswerkey = IPCR_MidtermAnswerKey_form(request.POST, prefix = "midtermanswerkey")   
        form_finaltermanswerkey = IPCR_FinaltermAnswerKey_form(request.POST, prefix = "finaltermanswerkey")   
        form_gradingsheet = IPCR_GradingSheet_form(request.POST, prefix = "form_gradingsheet")   
        form_studentadviced = IPCR_StudentAdviced_form(request.POST, prefix = "form_studentadviced")   
        form_accomplishmentreport = IPCR_AccomplishmentReport_form(request.POST, prefix = "form_accomplishmentreport")   
        form_researchproposalsubmitted = IPCR_ResearchProposalSubmitted_form(request.POST, prefix = "form_researchproposalsubmitted")   
        form_researchimplemented = IPCR_ResearchImplemented_form(request.POST, prefix = "form_researchimplemented")   
        form_researchpresented = IPCR_ResearchPresented_form(request.POST, prefix = "form_researchpresented")   
        form_researchpublished = IPCR_ResearchPublished_form(request.POST, prefix = "form_researchpublished")   
        form_approvediprights = IPCR_ApprovedIPRights_form(request.POST, prefix = "form_approvediprights")   
        form_researchutilized = IPCR_ResearchUtilized_form(request.POST, prefix = "form_researchutilized")    
        form_numberofcitations = IPCR_NumberOfCitations_form(request.POST, prefix = "form_numberofcitations")   
        form_extensionproposalsubmitted = IPCR_ExtensionProposalSubmitted_form(request.POST, prefix = "form_extensionproposalsubmitted")   
        form_persontrained = IPCR_PersonTrained_form(request.POST, prefix = "form_persontrained")   
        form_personavailedratedgood = IPCR_PersonAvailedRatedGood_form(request.POST, prefix = "form_personavailedratedgood")   
        form_persontrainedratedgood = IPCR_PersonTrainedRatedGood_form(request.POST, prefix = "form_persontrainedratedgood")          
        form_technicaladvice = IPCR_TechnicalAdvice_form(request.POST, prefix = "form_technicaladvice") 
        form_accomplishmentreportdeligatedassignment = IPCR_AccomplishmentReportDeligatedAssignment_form(request.POST, prefix = "form_accomplishmentreportdeligatedassignment")
        form_flagraisingattendance = IPCR_FlagRaisingAttendance_form(request.POST, prefix = "form_flagraisingattendance")        
        form_flagloweringattendance = IPCR_FlagLoweringAttendance_form(request.POST, prefix = "form_flagloweringattendance")          
        form_wellnessprogramattendance = IPCR_WellnessProgramAttendance_form(request.POST, prefix = "form_wellnessprogramattendance")          
        form_schoolcelebrationattendance = IPCR_SchoolCelebrationAttendance_form(request.POST, prefix = "form_schoolcelebrationattendance") 
        form_trainingattendance = IPCR_TrainingAttendance_form(request.POST, prefix = "form_trainingattendance") 
        form_facultymeetingattendance = IPCR_FacultyMeetingAttendance_form(request.POST, prefix = "form_facultymeetingattendance") 
        form_accreditationattendance = IPCR_AccreditationAttendance_form(request.POST, prefix = "form_accreditationattendance") 
        form_spiritualactivityattendance = IPCR_SpiritualActivityAttendance_form(request.POST, prefix = "form_spiritualactivityattendance") 
       
                   
        if (form_syllabus.is_valid() and form_courseguide.is_valid() and form_SLM.is_valid() and form_subjectareas.is_valid() and 
            form_attendancesheet.is_valid() and form_classrecord.is_valid() and form_classrecord.is_valid() and form_teachingeffectiveness.is_valid() and form_classroomobservation.is_valid() and
            form_midtermtosrubrics.is_valid() and form_finaltermtosrubrics.is_valid() and form_midtermtestquestions.is_valid() and
            form_finaltermtestquestions.is_valid() and form_midtermanswerkey.is_valid() and form_finaltermanswerkey.is_valid() and
            form_gradingsheet.is_valid() and form_studentadviced.is_valid() and form_accomplishmentreport.is_valid() and
            form_researchproposalsubmitted.is_valid() and form_researchimplemented.is_valid() and form_researchpresented.is_valid() and
            form_researchpublished.is_valid() and form_approvediprights.is_valid() and form_researchutilized.is_valid() and form_numberofcitations.is_valid() and
            form_extensionproposalsubmitted.is_valid() and form_persontrained.is_valid() and form_personavailedratedgood.is_valid() and
            form_persontrainedratedgood.is_valid() and form_technicaladvice.is_valid() and
            form_accomplishmentreportdeligatedassignment.is_valid() and form_flagraisingattendance.is_valid() and form_flagloweringattendance.is_valid() and
            form_wellnessprogramattendance.is_valid() and form_schoolcelebrationattendance.is_valid() and
            form_trainingattendance.is_valid() and form_facultymeetingattendance.is_valid() and form_accreditationattendance.is_valid() and
            form_spiritualactivityattendance.is_valid()):
            
            latest_submission.syllabus_Remarks = form_syllabus.cleaned_data['Syllabus_Remarks']
            latest_submission.CourseGuide_Remarks = form_courseguide.cleaned_data['CourseGuide_Remarks']
            latest_submission.SLM_Remarks = form_SLM.cleaned_data['SLM_Remarks']
            latest_submission.SubjectAreas_Remarks = form_subjectareas.cleaned_data['SubjectAreas_Remarks']
            latest_submission.AttendanceSheet_Remarks = form_attendancesheet.cleaned_data['AttendanceSheet_Remarks']
            latest_submission.ClassRecord_Remarks = form_classrecord.cleaned_data['ClassRecord_Remarks']
            latest_submission.TeachingEffectiveness_Remarks = form_teachingeffectiveness.cleaned_data['TeachingEffectiveness_Remarks']
            latest_submission.ClassroomObservation_Remarks = form_classroomobservation.cleaned_data['ClassroomObservation_Remarks']
            latest_submission.MidtermTOSRubrics_Remarks = form_midtermtosrubrics.cleaned_data['MidtermTOSRubrics_Remarks']
            latest_submission.FinaltermTOSRubrics_Remarks = form_finaltermtosrubrics.cleaned_data['FinaltermTOSRubrics_Remarks']
            latest_submission.MidtermTestQuestions_Remarks = form_midtermtestquestions.cleaned_data['MidtermTestQuestions_Remarks']
            latest_submission.FinaltermTestQuestions_Remarks = form_finaltermtestquestions.cleaned_data['FinaltermTestQuestions_Remarks']
            latest_submission.MidtermAnswerKey_Remarks = form_midtermanswerkey.cleaned_data['MidtermAnswerKey_Remarks']
            latest_submission.FinaltermAnswerKey_Remarks = form_finaltermanswerkey.cleaned_data['FinaltermAnswerKey_Remarks']
            latest_submission.GradingSheet_Remarks = form_gradingsheet.cleaned_data['GradingSheet_Remarks']
            latest_submission.StudentAdviced_Remarks = form_studentadviced.cleaned_data['StudentAdviced_Remarks']
            latest_submission.AccomplishmentReport_Remarks = form_accomplishmentreport.cleaned_data['AccomplishmentReport_Remarks']
            latest_submission.ResearchProposalSubmitted_Remarks = form_researchproposalsubmitted.cleaned_data['ResearchProposalSubmitted_Remarks']
            latest_submission.ResearchImplemented_Remarks = form_researchimplemented.cleaned_data['ResearchImplemented_Remarks']
            latest_submission.ResearchPresented_Remarks = form_researchpresented.cleaned_data['ResearchPresented_Remarks']
            latest_submission.ResearchPublished_Remarks = form_researchpublished.cleaned_data['ResearchPublished_Remarks']
            latest_submission.ApprovedIPRights_Remarks = form_approvediprights.cleaned_data['ApprovedIPRights_Remarks']
            latest_submission.ResearchUtilized_Remarks = form_researchutilized.cleaned_data['ResearchUtilized_Remarks']
            latest_submission.NumberOfCitations_Remarks = form_numberofcitations.cleaned_data['NumberOfCitations_Remarks']
            latest_submission.ExtensionProposalSubmitted_Remarks = form_extensionproposalsubmitted.cleaned_data['ExtensionProposalSubmitted_Remarks']
            latest_submission.PersonTrained_Remarks = form_persontrained.cleaned_data['PersonTrained_Remarks']
            latest_submission.PersonAvailedRatedGood_Remarks = form_personavailedratedgood.cleaned_data['PersonAvailedRatedGood_Remarks']
            latest_submission.PersonTrainedRatedGood_Remarks = form_persontrainedratedgood.cleaned_data['PersonTrainedRatedGood_Remarks']
            latest_submission.TechnicalAdvice_Remarks = form_technicaladvice.cleaned_data['TechnicalAdvice_Remarks']
            latest_submission.AccomplishmentReportDeligatedAssignment_Remarks = form_accomplishmentreportdeligatedassignment.cleaned_data['AccomplishmentReportDeligatedAssignment_Remarks']
            latest_submission.FlagRaisingAttendance_Remarks = form_flagraisingattendance.cleaned_data['FlagRaisingAttendance_Remarks']
            latest_submission.FlagLoweringAttendance_Remarks = form_flagloweringattendance.cleaned_data['FlagLoweringAttendance_Remarks']
            latest_submission.WellnessProgramAttendance_Remarks = form_wellnessprogramattendance.cleaned_data['WellnessProgramAttendance_Remarks']
            latest_submission.SchoolCelebrationAttendance_Remarks = form_schoolcelebrationattendance.cleaned_data['SchoolCelebrationAttendance_Remarks']
            latest_submission.TrainingAttendance_Remarks = form_trainingattendance.cleaned_data['TrainingAttendance_Remarks']
            latest_submission.FacultyMeetingAttendance_Remarks = form_facultymeetingattendance.cleaned_data['FacultyMeetingAttendance_Remarks']
            latest_submission.AccreditationAttendance_Remarks = form_accreditationattendance.cleaned_data['AccreditationAttendance_Remarks']
            latest_submission.SpiritualActivityAttendance_Remarks = form_spiritualactivityattendance.cleaned_data['SpiritualActivityAttendance_Remarks']
            latest_submission.save()

            return redirect('admin_faculty_list', username=username)
    else:
        form_syllabus = IPCR_Syllabus_form(prefix="form_syllabus", initial={'Syllabus_Remarks': initial_data['Syllabus_Remarks']})
        form_courseguide = IPCR_CourseGuide_form(prefix="form_courseguide", initial={'CourseGuide_Remarks': initial_data['CourseGuide_Remarks']})
        form_SLM = IPCR_SLM_form(prefix="form_SLM", initial={'SLM_Remarks': initial_data['SLM_Remarks']})
        form_subjectareas = IPCR_SubjectAreas_form(prefix="form_subjectareas", initial={'SubjectAreas_Remarks': initial_data['SubjectAreas_Remarks']})
        form_attendancesheet = IPCR_AttendanceSheet_form(prefix = "form_attendancesheet", initial={'AttendanceSheet_Remarks': initial_data['AttendanceSheet_Remarks']})              
        form_classrecord = IPCR_ClassRecord_form(prefix = "form_classrecord", initial={'ClassRecord_Remarks': initial_data['ClassRecord_Remarks']})              
        form_teachingeffectiveness = IPCR_TeachingEffectiveness_form(prefix = "form_teachingeffectiveness", initial={'TeachingEffectiveness_Remarks': initial_data['TeachingEffectiveness_Remarks']})   
        form_classroomobservation = IPCR_ClassroomObservation_form(prefix = "form_classroomobservation", initial={'ClassroomObservation_Remarks': initial_data['ClassroomObservation_Remarks']})   
        form_midtermtosrubrics = IPCR_MidtermTOSRubrics_form(prefix = "form_midtermtosrubrics", initial={'MidtermTOSRubrics_Remarks': initial_data['MidtermTOSRubrics_Remarks']})   
        form_finaltermtosrubrics = IPCR_FinaltermTOSRubrics_form(prefix = "form_finaltermtosrubrics", initial={'FinaltermTOSRubrics_Remarks': initial_data['FinaltermTOSRubrics_Remarks']})   
        form_midtermtestquestions = IPCR_MidtermTestQuestions_form(prefix = "midtermtestquestions", initial={'MidtermTestQuestions_Remarks': initial_data['MidtermTestQuestions_Remarks']})   
        form_finaltermtestquestions = IPCR_FinaltermTestQuestions_form(prefix = "finaltermtestquestions", initial={'FinaltermTestQuestions_Remarks': initial_data['FinaltermTestQuestions_Remarks']})   
        form_midtermanswerkey = IPCR_MidtermAnswerKey_form(prefix = "midtermanswerkey", initial={'MidtermAnswerKey_Remarks': initial_data['MidtermAnswerKey_Remarks']})   
        form_finaltermanswerkey = IPCR_FinaltermAnswerKey_form(prefix = "finaltermanswerkey", initial={'FinaltermAnswerKey_Remarks': initial_data['FinaltermAnswerKey_Remarks']})   
        form_gradingsheet = IPCR_GradingSheet_form(prefix = "form_gradingsheet", initial={'GradingSheet_Remarks': initial_data['GradingSheet_Remarks']})   
        form_studentadviced = IPCR_StudentAdviced_form(prefix = "form_studentadviced", initial={'StudentAdviced_Remarks': initial_data['StudentAdviced_Remarks']})   
        form_accomplishmentreport = IPCR_AccomplishmentReport_form(prefix = "form_accomplishmentreport", initial={'AccomplishmentReport_Remarks': initial_data['AccomplishmentReport_Remarks']})   
        form_researchproposalsubmitted = IPCR_ResearchProposalSubmitted_form(prefix = "form_researchproposalsubmitted", initial={'ResearchProposalSubmitted_Remarks': initial_data['ResearchProposalSubmitted_Remarks']})   
        form_researchimplemented = IPCR_ResearchImplemented_form(prefix = "form_researchimplemented", initial={'ResearchImplemented_Remarks': initial_data['ResearchImplemented_Remarks']})   
        form_researchpresented = IPCR_ResearchPresented_form(prefix = "form_researchpresented", initial={'ResearchPresented_Remarks': initial_data['ResearchPresented_Remarks']})   
        form_researchpublished = IPCR_ResearchPublished_form(prefix = "form_researchpublished", initial={'ResearchPublished_Remarks': initial_data['ResearchPublished_Remarks']})   
        form_approvediprights = IPCR_ApprovedIPRights_form(prefix = "form_approvediprights", initial={'ApprovedIPRights_Remarks': initial_data['ApprovedIPRights_Remarks']})   
        form_researchutilized = IPCR_ResearchUtilized_form(prefix = "form_researchutilized", initial={'ResearchUtilized_Remarks': initial_data['ResearchUtilized_Remarks']})    
        form_numberofcitations = IPCR_NumberOfCitations_form(prefix = "form_numberofcitations", initial={'NumberOfCitations_Remarks': initial_data['NumberOfCitations_Remarks']})   
        form_extensionproposalsubmitted = IPCR_ExtensionProposalSubmitted_form(prefix = "form_extensionproposalsubmitted", initial={'ExtensionProposalSubmitted_Remarks': initial_data['ExtensionProposalSubmitted_Remarks']})   
        form_persontrained = IPCR_PersonTrained_form(prefix = "form_persontrained", initial={'PersonTrained_Remarks': initial_data['PersonTrained_Remarks']})   
        form_personavailedratedgood = IPCR_PersonAvailedRatedGood_form(prefix = "form_personavailedratedgood", initial={'PersonAvailedRatedGood_Remarks': initial_data['PersonAvailedRatedGood_Remarks']})   
        form_persontrainedratedgood = IPCR_PersonTrainedRatedGood_form(prefix = "form_persontrainedratedgood", initial={'PersonTrainedRatedGood_Remarks': initial_data['PersonTrainedRatedGood_Remarks']})          
        form_technicaladvice = IPCR_TechnicalAdvice_form(prefix = "form_technicaladvice", initial={'TechnicalAdvice_Remarks': initial_data['TechnicalAdvice_Remarks']}) 
        form_accomplishmentreportdeligatedassignment = IPCR_AccomplishmentReportDeligatedAssignment_form(prefix = "form_accomplishmentreportdeligatedassignment", initial={'AccomplishmentReportDeligatedAssignment_Remarks': initial_data['AccomplishmentReportDeligatedAssignment_Remarks']})
        form_flagraisingattendance = IPCR_FlagRaisingAttendance_form(prefix = "form_flagraisingattendance", initial={'FlagRaisingAttendance_Remarks': initial_data['FlagRaisingAttendance_Remarks']})        
        form_flagloweringattendance = IPCR_FlagLoweringAttendance_form(prefix = "form_flagloweringattendance", initial={'FlagLoweringAttendance_Remarks': initial_data['FlagLoweringAttendance_Remarks']})          
        form_wellnessprogramattendance = IPCR_WellnessProgramAttendance_form(prefix = "form_wellnessprogramattendance", initial={'WellnessProgramAttendance_Remarks': initial_data['WellnessProgramAttendance_Remarks']})          
        form_schoolcelebrationattendance = IPCR_SchoolCelebrationAttendance_form(prefix = "form_schoolcelebrationattendance", initial={'SchoolCelebrationAttendance_Remarks': initial_data['SchoolCelebrationAttendance_Remarks']}) 
        form_trainingattendance = IPCR_TrainingAttendance_form(prefix = "form_trainingattendance", initial={'TrainingAttendance_Remarks': initial_data['TrainingAttendance_Remarks']}) 
        form_facultymeetingattendance = IPCR_FacultyMeetingAttendance_form(prefix = "form_facultymeetingattendance", initial={'FacultyMeetingAttendance_Remarks': initial_data['FacultyMeetingAttendance_Remarks']}) 
        form_accreditationattendance = IPCR_AccreditationAttendance_form(prefix = "form_accreditationattendance", initial={'AccreditationAttendance_Remarks': initial_data['AccreditationAttendance_Remarks']}) 
        form_spiritualactivityattendance = IPCR_SpiritualActivityAttendance_form(prefix = "form_spiritualactivityattendance", initial={'SpiritualActivityAttendance_Remarks': initial_data['SpiritualActivityAttendance_Remarks']}) 
             
        
    user_groups = request.user.groups.all()
    users_in_group = User.objects.filter(groups__in=user_groups).exclude(username=request.user.username).distinct()

    context = {
        'users_in_same_groups': users_in_group,
        'selected_author': selected_author,
        'form_syllabus': form_syllabus,
        'form_syllabus_target' : latest_submission.Syllabus_Target_submitted if latest_submission else '',
        'form_syllabus_accomplished' : latest_submission.Syllabus_Accomplished_submitted if latest_submission else '',
        'form_courseguide': form_courseguide,
        'form_courseguide_target' : latest_submission.CourseGuide_Target_submitted if latest_submission else '',
        'form_courseguide_accomplished' : latest_submission.CourseGuide_Accomplished_submitted if latest_submission else '',
        'form_SLM': form_SLM,
        'form_SLM_target' : latest_submission.SLM_Target_submitted if latest_submission else '',
        'form_SLM_accomplished' : latest_submission.SLM_Accomplished_submitted if latest_submission else '',
        'form_subjectareas': form_subjectareas,
        'form_subjectareas_target' : latest_submission.SubjectAreas_Target_submitted if latest_submission else '',
        'form_subjectareas_accomplished' : latest_submission.SubjectAreas_Accomplished_submitted if latest_submission else '',
        'form_attendancesheet' : form_attendancesheet,
        'form_attendancesheet_target' : latest_submission.AttendanceSheet_Target_submitted if latest_submission else '',
        'form_attendancesheet_accomplished' : latest_submission.AttendanceSheet_Accomplished_submitted if latest_submission else '',
        'form_classrecord' : form_classrecord,
        'form_classrecord_target' : latest_submission.ClassRecord_Target_submitted if latest_submission else '',
        'form_classrecord_accomplished' : latest_submission.ClassRecord_Accomplished_submitted if latest_submission else '', 
        'form_teachingeffectiveness' : form_teachingeffectiveness,
        'form_teachingeffectiveness_target' : latest_submission.TeachingEffectiveness_Target_submitted if latest_submission else '',
        'form_teachingeffectiveness_accomplished' : latest_submission.TeachingEffectiveness_Accomplished_submitted if latest_submission else '',         
        'form_classroomobservation' : form_classroomobservation,
        'form_classroomobservation_target' : latest_submission.ClassroomObservation_Target_submitted if latest_submission else '',
        'form_classroomobservation_accomplished' : latest_submission.ClassroomObservation_Accomplished_submitted if latest_submission else '',         
        'form_midtermtosrubrics' : form_midtermtosrubrics,
        'form_midtermtosrubrics_target' : latest_submission.MidtermTOSRubrics_Target_submitted if latest_submission else '',
        'form_midtermtosrubrics_accomplished' : latest_submission.MidtermTOSRubrics_Accomplished_submitted if latest_submission else '',         
        'form_finaltermtosrubrics' : form_finaltermtosrubrics,
        'form_finaltermtosrubrics_target' : latest_submission.FinaltermTOSRubrics_Target_submitted if latest_submission else '',
        'form_finaltermtosrubrics_accomplished' : latest_submission.FinaltermTOSRubrics_Accomplished_submitted if latest_submission else '',         
        'form_finaltermtosrubrics' : form_finaltermtosrubrics,
        'form_finaltermtosrubrics_target' : latest_submission.FinaltermTOSRubrics_Target_submitted if latest_submission else '',
        'form_finaltermtosrubrics_accomplished' : latest_submission.FinaltermTOSRubrics_Accomplished_submitted if latest_submission else '',         
        'form_midtermtestquestions' : form_midtermtestquestions,
        'form_midtermtestquestions_target' : latest_submission.MidtermTestQuestions_Target_submitted if latest_submission else '',
        'form_midtermtestquestions_accomplished' : latest_submission.MidtermTestQuestions_Accomplished_submitted if latest_submission else '',         
        'form_finaltermtestquestions' : form_finaltermtestquestions,
        'form_finaltermtestquestions_target' : latest_submission.FinaltermTestQuestions_Target_submitted if latest_submission else '',
        'form_finaltermtestquestions_accomplished' : latest_submission.FinaltermTestQuestions_Accomplished_submitted if latest_submission else '',         
        'form_midtermanswerkey' : form_midtermanswerkey,
        'form_midtermanswerkey_target' : latest_submission.MidtermAnswerKey_Target_submitted if latest_submission else '',
        'form_midtermanswerkey_accomplished' : latest_submission.MidtermAnswerKey_Accomplished_submitted if latest_submission else '',         
        'form_finaltermanswerkey' : form_finaltermanswerkey,
        'form_finaltermanswerkey_target' : latest_submission.FinaltermAnswerKey_Target_submitted if latest_submission else '',
        'form_finaltermanswerkey_accomplished' : latest_submission.FinaltermAnswerKey_Accomplished_submitted if latest_submission else '',         
        'form_gradingsheet' : form_gradingsheet,
        'form_gradingsheet_target' : latest_submission.GradingSheet_Target_submitted if latest_submission else '',
        'form_gradingsheet_accomplished' : latest_submission.GradingSheet_Accomplished_submitted if latest_submission else '',
        'form_studentadviced' : form_studentadviced,
        'form_studentadviced_target' : latest_submission.StudentAdviced_Target_submitted if latest_submission else '',
        'form_studentadviced_accomplished' : latest_submission.StudentAdviced_Accomplished_submitted if latest_submission else '',
        'form_accomplishmentreport' : form_accomplishmentreport,
        'form_accomplishmentreport_target' : latest_submission.AccomplishmentReport_Target_submitted if latest_submission else '',
        'form_accomplishmentreport_accomplished' : latest_submission.AccomplishmentReport_Accomplished_submitted if latest_submission else '',
        'form_researchproposalsubmitted' : form_researchproposalsubmitted,
        'form_researchproposalsubmitted_target' : latest_submission.ResearchProposalSubmitted_Target_submitted if latest_submission else '',
        'form_researchproposalsubmitted_accomplished' : latest_submission.ResearchProposalSubmitted_Accomplished_submitted if latest_submission else '',
        'form_researchimplemented' : form_researchimplemented,
        'form_researchimplemented_target' : latest_submission.ResearchImplemented_Target_submitted if latest_submission else '',
        'form_researchimplemented_accomplished' : latest_submission.ResearchImplemented_Accomplished_submitted if latest_submission else '',
        'form_researchpresented' : form_researchpresented,
        'form_researchpresented_target' : latest_submission.ResearchPresented_Target_submitted if latest_submission else '',
        'form_researchpresented_accomplished' : latest_submission.ResearchPresented_Accomplished_submitted if latest_submission else '',
        'form_researchpublished' : form_researchpublished,
        'form_researchpublished_target' : latest_submission.ResearchPublished_Target_submitted if latest_submission else '',
        'form_researchpublished_accomplished' : latest_submission.ResearchPublished_Accomplished_submitted if latest_submission else '',
        'form_approvediprights' : form_approvediprights,
        'form_approvediprights_target' : latest_submission.ApprovedIPRights_Target_submitted if latest_submission else '',
        'form_approvediprights_accomplished' : latest_submission.ApprovedIPRights_Accomplished_submitted if latest_submission else '',
        'form_researchutilized' : form_researchutilized,
        'form_researchutilized_target' : latest_submission.ResearchUtilized_Target_submitted if latest_submission else '',
        'form_researchutilized_accomplished' : latest_submission.ResearchUtilized_Accomplished_submitted if latest_submission else '',
        'form_numberofcitations' : form_numberofcitations,
        'form_numberofcitations_target' : latest_submission.NumberOfCitations_Target_submitted if latest_submission else '',
        'form_numberofcitations_accomplished' : latest_submission.NumberOfCitations_Accomplished_submitted if latest_submission else '',
        'form_extensionproposalsubmitted' : form_extensionproposalsubmitted,
        'form_extensionproposalsubmitted_target' : latest_submission.ExtensionProposalSubmitted_Target_submitted if latest_submission else '',
        'form_extensionproposalsubmitted_accomplished' : latest_submission.ExtensionProposalSubmitted_Accomplished_submitted if latest_submission else '',
        'form_persontrained' : form_persontrained,
        'form_persontrained_target' : latest_submission.PersonTrained_Target_submitted if latest_submission else '',
        'form_persontrained_accomplished' : latest_submission.PersonTrained_Accomplished_submitted if latest_submission else '',
        'form_personavailedratedgood' : form_personavailedratedgood,
        'form_personavailedratedgood_target' : latest_submission.PersonAvailedRatedGood_Target_submitted if latest_submission else '',
        'form_personavailedratedgood_accomplished' : latest_submission.PersonAvailedRatedGood_Accomplished_submitted if latest_submission else '',
        'form_persontrainedratedgood' : form_persontrainedratedgood,
        'form_persontrainedratedgood_target' : latest_submission.PersonTrainedRatedGood_Target_submitted if latest_submission else '',
        'form_persontrainedratedgood_accomplished' : latest_submission.PersonTrainedRatedGood_Accomplished_submitted if latest_submission else '',
        'form_technicaladvice' : form_technicaladvice,
        'form_technicaladvice_target' : latest_submission.TechnicalAdvice_Target_submitted if latest_submission else '',
        'form_technicaladvice_accomplished' : latest_submission.TechnicalAdvice_Accomplished_submitted if latest_submission else '',
        'form_accomplishmentreportdeligatedassignment' : form_accomplishmentreportdeligatedassignment,
        'form_accomplishmentreportdeligatedassignment_target' : latest_submission.AccomplishmentReportDeligatedAssignment_Target_submitted if latest_submission else '',
        'form_accomplishmentreportdeligatedassignment_accomplished' : latest_submission.AccomplishmentReportDeligatedAssignment_Accomplished_submitted if latest_submission else '',
        'form_flagraisingattendance' : form_flagraisingattendance,
        'form_flagraisingattendance_target' : latest_submission.FlagRaisingAttendance_Target_submitted if latest_submission else '',
        'form_flagraisingattendance_accomplished' : latest_submission.FlagRaisingAttendance_Accomplished_submitted if latest_submission else '',
        'form_flagloweringattendance' : form_flagloweringattendance,
        'form_flagloweringattendance_target' : latest_submission.FlagLoweringAttendance_Target_submitted if latest_submission else '',
        'form_flagloweringattendance_accomplished' : latest_submission.FlagLoweringAttendance_Accomplished_submitted if latest_submission else '',
        'form_wellnessprogramattendance' : form_wellnessprogramattendance,
        'form_wellnessprogramattendance_target' : latest_submission.WellnessProgramAttendance_Target_submitted if latest_submission else '',
        'form_wellnessprogramattendance_accomplished' : latest_submission.WellnessProgramAttendance_Accomplished_submitted if latest_submission else '',
        'form_schoolcelebrationattendance' : form_schoolcelebrationattendance,
        'form_schoolcelebrationattendance_target' : latest_submission.SchoolCelebrationAttendance_Target_submitted if latest_submission else '',
        'form_schoolcelebrationattendance_accomplished' : latest_submission.SchoolCelebrationAttendance_Accomplished_submitted if latest_submission else '',
        'form_trainingattendance' : form_trainingattendance,
        'form_trainingattendance_target' : latest_submission.TrainingAttendance_Target_submitted if latest_submission else '',
        'form_trainingattendance_accomplished' : latest_submission.TrainingAttendance_Accomplished_submitted if latest_submission else '',
        'form_facultymeetingattendance' : form_facultymeetingattendance,
        'form_facultymeetingattendance_target' : latest_submission.FacultyMeetingAttendance_Target_submitted if latest_submission else '',
        'form_facultymeetingattendance_accomplished' : latest_submission.FacultyMeetingAttendance_Accomplished_submitted if latest_submission else '',
        'form_accreditationattendance' : form_accreditationattendance,
        'form_accreditationattendance_target' : latest_submission.AccreditationAttendance_Target_submitted if latest_submission else '',
        'form_accreditationattendance_accomplished' : latest_submission.AccreditationAttendance_Accomplished_submitted if latest_submission else '',
        'form_spiritualactivityattendance' : form_spiritualactivityattendance,
        'form_spiritualactivityattendance_target' : latest_submission.SpiritualActivityAttendance_Target_submitted if latest_submission else '',
        'form_spiritualactivityattendance_accomplished' : latest_submission.SpiritualActivityAttendance_Accomplished_submitted if latest_submission else ''
    }
    return render(request, 'forms/IPCRForm_Remarks.html', context)