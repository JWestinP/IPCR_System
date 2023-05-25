from django.shortcuts import render
from forms.forms import *
from forms.models import *


# Create your views here.
def download(request):
    return render(request, ('downloads/IPCR_Download.html'))

def Show_IPCR(request):
    Current_user = request.user
    IPCR_Deadline = IPCR_Deadline_model.objects.all().order_by('-id').first()
    IPCR_Syllabus = IPCR_Syllabus_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_CourseGuide = IPCR_CourseGuide_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_slm = IPCR_SLM_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_SubjectAreas = IPCR_SubjectAreas_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_AttendanceSheet = IPCR_AttendanceSheet_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_ClassRecord = IPCR_ClassRecord_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_TeachingEffectiveness = IPCR_TeachingEffectiveness_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_ClassroomObservation = IPCR_ClassroomObservation_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_MidtermTOSRubrics = IPCR_MidtermTOSRubrics_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_FinaltermTOSRubrics = IPCR_FinaltermTOSRubrics_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_MidtermTestQuestions = IPCR_MidtermTestQuestions_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_FinaltermTestQuestions = IPCR_FinaltermTestQuestions_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_MidtermAnswerKey = IPCR_MidtermAnswerKey_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_FinaltermAnswerKey = IPCR_FinaltermAnswerKey_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_GradingSheet = IPCR_GradingSheet_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_StudentAdviced = IPCR_StudentAdviced_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_AccomplishmentReport = IPCR_AccomplishmentReport_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_ResearchProposalSubmitted = IPCR_ResearchProposalSubmitted_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_ResearchImplemented = IPCR_ResearchImplemented_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_ResearchPresented = IPCR_ResearchPresented_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_ResearchPublished = IPCR_ResearchPublished_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_ApprovedIPRights = IPCR_ApprovedIPRights_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_ResearchUtilized = IPCR_ResearchUtilized_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_NumberOfCitations = IPCR_NumberOfCitations_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_ExtensionProposalSubmitted = IPCR_ExtensionProposalSubmitted_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_PersonTrained = IPCR_PersonTrained_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_PersonAvailedRatedGood = IPCR_PersonAvailedRatedGood_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_PersonTrainedRatedGood = IPCR_PersonTrainedRatedGood_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_TechnicalAdvice = IPCR_TechnicalAdvice_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_AccomplishmentReportDeligatedAssignment = IPCR_AccomplishmentReportDeligatedAssignment_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_FlagRaisingAttendance = IPCR_FlagRaisingAttendance_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_FlagLoweringAttendance = IPCR_FlagLoweringAttendance_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_WellnessProgramAttendance = IPCR_WellnessProgramAttendance_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_SchoolCelebrationAttendance = IPCR_SchoolCelebrationAttendance_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_TrainingAttendance = IPCR_TrainingAttendance_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_FacultyMeetingAttendance = IPCR_FacultyMeetingAttendance_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_AccreditationAttendance = IPCR_AccomplishmentReport_model.objects.filter(author=Current_user).order_by('-id').first()
    IPCR_SpiritualActivityAttendance = IPCR_SpiritualActivityAttendance_model.objects.filter(author=Current_user).order_by('-id').first()
    print (IPCR_Syllabus)
    return render (request, 'downloads/IPCRForm_View.html', {'IPCR_Syllabus' : IPCR_Syllabus, 'IPCR_Deadline' : IPCR_Deadline, 'IPCR_CourseGuide' : IPCR_CourseGuide,
                                                         'IPCR_SLM' : IPCR_slm, 'IPCR_SubjectAreas' : IPCR_SubjectAreas, 'IPCR_AttendanceSheet' : IPCR_AttendanceSheet,
                                                         'IPCR_ClassRecord' : IPCR_ClassRecord, 'IPCR_TeachingEffectiveness' : IPCR_TeachingEffectiveness, 'IPCR_ClassroomObservation' : IPCR_ClassroomObservation,
                                                         'IPCR_MidtermTOSRubrics' : IPCR_MidtermTOSRubrics, 'IPCR_FinaltermTOSRubrics' : IPCR_FinaltermTOSRubrics, 'IPCR_MidtermTestQuestions' : IPCR_MidtermTestQuestions,
                                                         'IPCR_FinaltermTestQuestions' : IPCR_FinaltermTestQuestions, 'IPCR_MidtermAnswerKey' : IPCR_MidtermAnswerKey, "IPCR_FinaltermAnswerKey" : IPCR_FinaltermAnswerKey,
                                                         'IPCR_GradingSheet' : IPCR_GradingSheet, 'IPCR_StudentAdviced' : IPCR_StudentAdviced, 'IPCR_AccomplishmentReport' : IPCR_AccomplishmentReport,
                                                         'IPCR_ResearchProposalSubmitted' : IPCR_ResearchProposalSubmitted, 'IPCR_ResearchImplemented' : IPCR_ResearchImplemented, 'IPCR_ResearchPresented' : IPCR_ResearchPresented,
                                                         'IPCR_ResearchPublished' : IPCR_ResearchPublished, 'IPCR_ApprovedIPRights' : IPCR_ApprovedIPRights, 'IPCR_ResearchUtilized' : IPCR_ResearchUtilized, 'IPCR_NumberOfCitations' : IPCR_NumberOfCitations,
                                                         'IPCR_ExtensionProposalSubmitted' : IPCR_ExtensionProposalSubmitted, 'IPCR_PersonTrained' : IPCR_PersonTrained, 'IPCR_PersonAvailedRatedGood' : IPCR_PersonAvailedRatedGood,
                                                         'IPCR_PersonTrainedRatedGood' : IPCR_PersonTrainedRatedGood, 'IPCR_TechnicalAdvice' : IPCR_TechnicalAdvice, 'IPCR_AccomplishmentReportDeligatedAssignment' : IPCR_AccomplishmentReportDeligatedAssignment,
                                                         'IPCR_FlagRaisingAttendance' : IPCR_FlagRaisingAttendance, 'IPCR_FlagLoweringAttendance' : IPCR_FlagLoweringAttendance, 'IPCR_WellnessProgramAttendance' : IPCR_WellnessProgramAttendance,
                                                         'IPCR_SchoolCelebrationAttendance' : IPCR_SchoolCelebrationAttendance, 'IPCR_TrainingAttendance' : IPCR_TrainingAttendance, 'IPCR_FacultyMeetingAttendance' : IPCR_FacultyMeetingAttendance,
                                                         'IPCR_AccreditationAttendance' : IPCR_AccreditationAttendance, 'IPCR_SpiritualActivityAttendance' : IPCR_SpiritualActivityAttendance})

def Show_Submitted_IPCR(request):
    latest_submission = IPCR_Submit_model.objects.filter(author=request.user).latest('id')
    latest_deadline = IPCR_Deadline_model.objects.all().latest('id')
    context = {
        'form_deadline': latest_deadline.IPCR_Deadline if latest_deadline else '',
        'form_syllabus': latest_submission.syllabus_Remarks if latest_submission else '',
        'form_syllabus_target' : latest_submission.Syllabus_Target_submitted if latest_submission else '',
        'form_syllabus_accomplished' : latest_submission.Syllabus_Accomplished_submitted if latest_submission else '',
        'form_courseguide': latest_submission.CourseGuide_Remarks if latest_submission else '',
        'form_courseguide_target' : latest_submission.CourseGuide_Target_submitted if latest_submission else '',
        'form_courseguide_accomplished' : latest_submission.CourseGuide_Accomplished_submitted if latest_submission else '',
        'form_SLM': latest_submission.SLM_Remarks if latest_submission else '',
        'form_SLM_target' : latest_submission.SLM_Target_submitted if latest_submission else '',
        'form_SLM_accomplished' : latest_submission.SLM_Accomplished_submitted if latest_submission else '',
        'form_subjectareas': latest_submission.SubjectAreas_Remarks if latest_submission else '',
        'form_subjectareas_target' : latest_submission.SubjectAreas_Target_submitted if latest_submission else '',
        'form_subjectareas_accomplished' : latest_submission.SubjectAreas_Accomplished_submitted if latest_submission else '',
        'form_attendancesheet' : latest_submission.AttendanceSheet_Remarks if latest_submission else '',
        'form_attendancesheet_target' : latest_submission.AttendanceSheet_Target_submitted if latest_submission else '',
        'form_attendancesheet_accomplished' : latest_submission.AttendanceSheet_Accomplished_submitted if latest_submission else '',
        'form_classrecord' : latest_submission.ClassRecord_Remarks if latest_submission else '',
        'form_classrecord_target' : latest_submission.ClassRecord_Target_submitted if latest_submission else '',
        'form_classrecord_accomplished' : latest_submission.ClassRecord_Accomplished_submitted if latest_submission else '', 
        'form_teachingeffectiveness' : latest_submission.TeachingEffectiveness_Remarks if latest_submission else '',
        'form_teachingeffectiveness_target' : latest_submission.TeachingEffectiveness_Target_submitted if latest_submission else '',
        'form_teachingeffectiveness_accomplished' : latest_submission.TeachingEffectiveness_Accomplished_submitted if latest_submission else '',         
        'form_classroomobservation' : latest_submission.ClassroomObservation_Remarks if latest_submission else '',
        'form_classroomobservation_target' : latest_submission.ClassroomObservation_Target_submitted if latest_submission else '',
        'form_classroomobservation_accomplished' : latest_submission.ClassroomObservation_Accomplished_submitted if latest_submission else '',         
        'form_midtermtosrubrics' : latest_submission.MidtermTOSRubrics_Remarks if latest_submission else '',
        'form_midtermtosrubrics_target' : latest_submission.MidtermTOSRubrics_Target_submitted if latest_submission else '',
        'form_midtermtosrubrics_accomplished' : latest_submission.MidtermTOSRubrics_Accomplished_submitted if latest_submission else '',         
        'form_finaltermtosrubrics' : latest_submission.FinaltermTOSRubrics_Remarks if latest_submission else '',
        'form_finaltermtosrubrics_target' : latest_submission.FinaltermTOSRubrics_Target_submitted if latest_submission else '',
        'form_finaltermtosrubrics_accomplished' : latest_submission.FinaltermTOSRubrics_Accomplished_submitted if latest_submission else '',         
        'form_finaltermtosrubrics' : latest_submission.FinaltermTOSRubrics_Remarks if latest_submission else '',
        'form_finaltermtosrubrics_target' : latest_submission.FinaltermTOSRubrics_Target_submitted if latest_submission else '',
        'form_finaltermtosrubrics_accomplished' : latest_submission.FinaltermTOSRubrics_Accomplished_submitted if latest_submission else '',         
        'form_midtermtestquestions' : latest_submission.MidtermTestQuestions_Remarks if latest_submission else '',
        'form_midtermtestquestions_target' : latest_submission.MidtermTestQuestions_Target_submitted if latest_submission else '',
        'form_midtermtestquestions_accomplished' : latest_submission.MidtermTestQuestions_Accomplished_submitted if latest_submission else '',         
        'form_finaltermtestquestions' : latest_submission.FinaltermTestQuestions_Remarks if latest_submission else '',
        'form_finaltermtestquestions_target' : latest_submission.FinaltermTestQuestions_Target_submitted if latest_submission else '',
        'form_finaltermtestquestions_accomplished' : latest_submission.FinaltermTestQuestions_Accomplished_submitted if latest_submission else '',         
        'form_midtermanswerkey' : latest_submission.MidtermAnswerKey_Remarks if latest_submission else '',
        'form_midtermanswerkey_target' : latest_submission.MidtermAnswerKey_Target_submitted if latest_submission else '',
        'form_midtermanswerkey_accomplished' : latest_submission.MidtermAnswerKey_Accomplished_submitted if latest_submission else '',         
        'form_finaltermanswerkey' : latest_submission.FinaltermAnswerKey_Remarks if latest_submission else '',
        'form_finaltermanswerkey_target' : latest_submission.FinaltermAnswerKey_Target_submitted if latest_submission else '',
        'form_finaltermanswerkey_accomplished' : latest_submission.FinaltermAnswerKey_Accomplished_submitted if latest_submission else '',         
        'form_gradingsheet' : latest_submission.GradingSheet_Remarks if latest_submission else '',
        'form_gradingsheet_target' : latest_submission.GradingSheet_Target_submitted if latest_submission else '',
        'form_gradingsheet_accomplished' : latest_submission.GradingSheet_Accomplished_submitted if latest_submission else '',
        'form_studentadviced' : latest_submission.StudentAdviced_Remarks if latest_submission else '',
        'form_studentadviced_target' : latest_submission.StudentAdviced_Target_submitted if latest_submission else '',
        'form_studentadviced_accomplished' : latest_submission.StudentAdviced_Accomplished_submitted if latest_submission else '',
        'form_accomplishmentreport' : latest_submission.AccomplishmentReport_Remarks if latest_submission else '',
        'form_accomplishmentreport_target' : latest_submission.AccomplishmentReport_Target_submitted if latest_submission else '',
        'form_accomplishmentreport_accomplished' : latest_submission.AccomplishmentReport_Accomplished_submitted if latest_submission else '',
        'form_researchproposalsubmitted' : latest_submission.ResearchProposalSubmitted_Remarks if latest_submission else '',
        'form_researchproposalsubmitted_target' : latest_submission.ResearchProposalSubmitted_Target_submitted if latest_submission else '',
        'form_researchproposalsubmitted_accomplished' : latest_submission.ResearchProposalSubmitted_Accomplished_submitted if latest_submission else '',
        'form_researchimplemented' : latest_submission.ResearchImplemented_Remarks if latest_submission else '',
        'form_researchimplemented_target' : latest_submission.ResearchImplemented_Target_submitted if latest_submission else '',
        'form_researchimplemented_accomplished' : latest_submission.ResearchImplemented_Accomplished_submitted if latest_submission else '',
        'form_researchpresented' : latest_submission.ResearchPresented_Remarks if latest_submission else '',
        'form_researchpresented_target' : latest_submission.ResearchPresented_Target_submitted if latest_submission else '',
        'form_researchpresented_accomplished' : latest_submission.ResearchPresented_Accomplished_submitted if latest_submission else '',
        'form_researchpublished' : latest_submission.ResearchPublished_Remarks if latest_submission else '',
        'form_researchpublished_target' : latest_submission.ResearchPublished_Target_submitted if latest_submission else '',
        'form_researchpublished_accomplished' : latest_submission.ResearchPublished_Accomplished_submitted if latest_submission else '',
        'form_approvediprights' : latest_submission.ApprovedIPRights_Remarks if latest_submission else '',
        'form_approvediprights_target' : latest_submission.ApprovedIPRights_Target_submitted if latest_submission else '',
        'form_approvediprights_accomplished' : latest_submission.ApprovedIPRights_Accomplished_submitted if latest_submission else '',
        'form_researchutilized' : latest_submission.ResearchUtilized_Remarks if latest_submission else '',
        'form_researchutilized_target' : latest_submission.ResearchUtilized_Target_submitted if latest_submission else '',
        'form_researchutilized_accomplished' : latest_submission.ResearchUtilized_Accomplished_submitted if latest_submission else '',
        'form_numberofcitations' : latest_submission.NumberOfCitations_Remarks if latest_submission else '',
        'form_numberofcitations_target' : latest_submission.NumberOfCitations_Target_submitted if latest_submission else '',
        'form_numberofcitations_accomplished' : latest_submission.NumberOfCitations_Accomplished_submitted if latest_submission else '',
        'form_extensionproposalsubmitted' : latest_submission.ExtensionProposalSubmitted_Remarks if latest_submission else '',
        'form_extensionproposalsubmitted_target' : latest_submission.ExtensionProposalSubmitted_Target_submitted if latest_submission else '',
        'form_extensionproposalsubmitted_accomplished' : latest_submission.ExtensionProposalSubmitted_Accomplished_submitted if latest_submission else '',
        'form_persontrained' : latest_submission.PersonTrained_Remarks if latest_submission else '',
        'form_persontrained_target' : latest_submission.PersonTrained_Target_submitted if latest_submission else '',
        'form_persontrained_accomplished' : latest_submission.PersonTrained_Accomplished_submitted if latest_submission else '',
        'form_personavailedratedgood' : latest_submission.PersonAvailedRatedGood_Remarks if latest_submission else '',
        'form_personavailedratedgood_target' : latest_submission.PersonAvailedRatedGood_Target_submitted if latest_submission else '',
        'form_personavailedratedgood_accomplished' : latest_submission.PersonAvailedRatedGood_Accomplished_submitted if latest_submission else '',
        'form_persontrainedratedgood' : latest_submission.PersonTrainedRatedGood_Remarks if latest_submission else '',
        'form_persontrainedratedgood_target' : latest_submission.PersonTrainedRatedGood_Target_submitted if latest_submission else '',
        'form_persontrainedratedgood_accomplished' : latest_submission.PersonTrainedRatedGood_Accomplished_submitted if latest_submission else '',
        'form_technicaladvice' : latest_submission.TechnicalAdvice_Remarks if latest_submission else '',
        'form_technicaladvice_target' : latest_submission.TechnicalAdvice_Target_submitted if latest_submission else '',
        'form_technicaladvice_accomplished' : latest_submission.TechnicalAdvice_Accomplished_submitted if latest_submission else '',
        'form_accomplishmentreportdeligatedassignment' : latest_submission.AccomplishmentReportDeligatedAssignment_Remarks if latest_submission else '',
        'form_accomplishmentreportdeligatedassignment_target' : latest_submission.AccomplishmentReportDeligatedAssignment_Target_submitted if latest_submission else '',
        'form_accomplishmentreportdeligatedassignment_accomplished' : latest_submission.AccomplishmentReportDeligatedAssignment_Accomplished_submitted if latest_submission else '',
        'form_flagraisingattendance' : latest_submission.FlagRaisingAttendance_Remarks if latest_submission else '',
        'form_flagraisingattendance_target' : latest_submission.FlagRaisingAttendance_Target_submitted if latest_submission else '',
        'form_flagraisingattendance_accomplished' : latest_submission.FlagRaisingAttendance_Accomplished_submitted if latest_submission else '',
        'form_flagloweringattendance' : latest_submission.FlagLoweringAttendance_Remarks if latest_submission else '',
        'form_flagloweringattendance_target' : latest_submission.FlagLoweringAttendance_Target_submitted if latest_submission else '',
        'form_flagloweringattendance_accomplished' : latest_submission.FlagLoweringAttendance_Accomplished_submitted if latest_submission else '',
        'form_wellnessprogramattendance' : latest_submission.WellnessProgramAttendance_Remarks if latest_submission else '',
        'form_wellnessprogramattendance_target' : latest_submission.WellnessProgramAttendance_Target_submitted if latest_submission else '',
        'form_wellnessprogramattendance_accomplished' : latest_submission.WellnessProgramAttendance_Accomplished_submitted if latest_submission else '',
        'form_schoolcelebrationattendance' : latest_submission.SchoolCelebrationAttendance_Remarks if latest_submission else '',
        'form_schoolcelebrationattendance_target' : latest_submission.SchoolCelebrationAttendance_Target_submitted if latest_submission else '',
        'form_schoolcelebrationattendance_accomplished' : latest_submission.SchoolCelebrationAttendance_Accomplished_submitted if latest_submission else '',
        'form_trainingattendance' : latest_submission.TrainingAttendance_Remarks if latest_submission else '',
        'form_trainingattendance_target' : latest_submission.TrainingAttendance_Target_submitted if latest_submission else '',
        'form_trainingattendance_accomplished' : latest_submission.TrainingAttendance_Accomplished_submitted if latest_submission else '',
        'form_facultymeetingattendance' : latest_submission.FacultyMeetingAttendance_Remarks if latest_submission else '',
        'form_facultymeetingattendance_target' : latest_submission.FacultyMeetingAttendance_Target_submitted if latest_submission else '',
        'form_facultymeetingattendance_accomplished' : latest_submission.FacultyMeetingAttendance_Accomplished_submitted if latest_submission else '',
        'form_accreditationattendance' : latest_submission.AccreditationAttendance_Remarks if latest_submission else '',
        'form_accreditationattendance_target' : latest_submission.AccreditationAttendance_Target_submitted if latest_submission else '',
        'form_accreditationattendance_accomplished' : latest_submission.AccreditationAttendance_Accomplished_submitted if latest_submission else '',
        'form_spiritualactivityattendance' : latest_submission.SpiritualActivityAttendance_Remarks if latest_submission else '',
        'form_spiritualactivityattendance_target' : latest_submission.SpiritualActivityAttendance_Target_submitted if latest_submission else '',
        'form_spiritualactivityattendance_accomplished' : latest_submission.SpiritualActivityAttendance_Accomplished_submitted if latest_submission else ''
    }
    return render(request, 'downloads/IPCRForm_Submitted_View.html', context)