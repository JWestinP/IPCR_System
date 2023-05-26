from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class IPCR_Form_model (models.Model):
    syllabus_Target = models.IntegerField(null = True, blank = True)
    syllabus_Accomplished = models.IntegerField(null = True, blank = True)
    CourseGuide_Target = models.IntegerField(null = True, blank = True)
    CourseGuide_Accomplished = models.IntegerField(null = True, blank = True)
    SLM_Target = models.IntegerField(null = True, blank = True)
    SLM_Accomplished = models.IntegerField(null = True, blank = True)
    SubjectAreas_Target = models.IntegerField(null = True, blank = True)
    SubjectAreas_Accomplished = models.IntegerField(null = True, blank = True)
    AttendanceSheet_Target = models.IntegerField(null = True, blank = True)
    AttendanceSheet_Accomplished = models.IntegerField(null = True, blank = True)
    ClassRecord_Target = models.IntegerField(null = True, blank = True)
    ClassRecord_Accomplished = models.IntegerField(null = True, blank = True)
    TeachingEffectiveness_Target = models.IntegerField(null = True, blank = True)
    TeachingEffectiveness_Accomplished = models.IntegerField(null = True, blank = True)
    ClassroomObservation_Target = models.IntegerField(null = True, blank = True)
    ClassroomObservation_Accomplished = models.IntegerField(null = True, blank = True)
    MidtermTOSRubrics_Target = models.IntegerField(null = True, blank = True)
    MidtermTOSRubrics_Accomplished = models.IntegerField(null = True, blank = True)
    FinaltermTOSRubrics_Target = models.IntegerField(null = True, blank = True)
    FinaltermTOSRubrics_Accomplished = models.IntegerField(null = True, blank = True)
    MidtermTestQuestions_Target = models.IntegerField(null = True, blank = True)
    MidtermTestQuestions_Accomplished = models.IntegerField(null = True, blank = True)
    FinaltermTestQuestions_Target = models.IntegerField(null = True, blank = True)
    FinaltermTestQuestions_Accomplished = models.IntegerField(null = True, blank = True)
    MidtermAnswerKey_Target = models.IntegerField(null = True, blank = True)
    MidtermAnswerKey_Accomplished = models.IntegerField(null = True, blank = True)
    FinaltermAnswerKey_Target = models.IntegerField(null = True, blank = True)
    FinaltermAnswerKey_Accomplished = models.IntegerField(null = True, blank = True)
    GradingSheet_Target = models.IntegerField(null = True, blank = True)
    GradingSheet_Accomplished = models.IntegerField(null = True, blank = True)
    StudentAdviced_Target = models.IntegerField(null = True, blank = True)
    StudentAdviced_Accomplished = models.IntegerField(null = True, blank = True)
    AccomplishmentReport_Target = models.IntegerField(null = True, blank = True)
    AccomplishmentReport_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchProposalSubmitted_Target = models.IntegerField(null = True, blank = True)
    ResearchProposalSubmitted_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchImplemented_Target = models.IntegerField(null = True, blank = True)
    ResearchImplemented_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchPresented_Target = models.IntegerField(null = True, blank = True)
    ResearchPresented_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchPublished_Target = models.IntegerField(null = True, blank = True)
    ResearchPublished_Accomplished = models.IntegerField(null = True, blank = True)
    ApprovedIPRights_Target = models.IntegerField(null = True, blank = True)
    ApprovedIPRights_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchUtilized_Target = models.IntegerField(null = True, blank = True)
    ResearchUtilized_Accomplished = models.IntegerField(null = True, blank = True)
    NumberOfCitations_Target = models.IntegerField(null = True, blank = True)
    NumberOfCitations_Accomplished = models.IntegerField(null = True, blank = True)
    ExtensionProposalSubmitted_Target = models.IntegerField(null = True, blank = True)
    ExtensionProposalSubmitted_Accomplished = models.IntegerField(null = True, blank = True)
    PersonTrained_Target = models.IntegerField(null = True, blank = True)
    PersonTrained_Accomplished = models.IntegerField(null = True, blank = True)
    PersonAvailedRatedGood_Target = models.IntegerField(null = True, blank = True)
    PersonAvailedRatedGood_Accomplished = models.IntegerField(null = True, blank = True)
    PersonTrainedRatedGood_Target = models.IntegerField(null = True, blank = True)
    PersonTrainedRatedGood_Accomplished = models.IntegerField(null = True, blank = True)
    TechnicalAdvice_Target = models.IntegerField(null = True, blank = True)
    TechnicalAdvice_Accomplished = models.IntegerField(null = True, blank = True)
    AccomplishmentReportDeligatedAssignment_Target = models.IntegerField(null = True, blank = True)
    AccomplishmentReportDeligatedAssignment_Accomplished = models.IntegerField(null = True, blank = True)
    FlagRaisingAttendance_Target = models.IntegerField(null = True, blank = True)
    FlagRaisingAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    FlagLoweringAttendance_Target = models.IntegerField(null = True, blank = True)
    FlagLoweringAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    WellnessProgramAttendance_Target = models.IntegerField(null = True, blank = True)
    WellnessProgramAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    SchoolCelebrationAttendance_Target = models.IntegerField(null = True, blank = True)
    SchoolCelebrationAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    TrainingAttendance_Target = models.IntegerField(null = True, blank = True)
    TrainingAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    FacultyMeetingAttendance_Target = models.IntegerField(null = True, blank = True)
    FacultyMeetingAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    AccreditationAttendance_Target = models.IntegerField(null = True, blank = True)
    AccreditationAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    SpiritualActivityAttendance_Target = models.IntegerField(null = True, blank = True)
    SpiritualActivityAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    
    IPCR_Submitted = models.DateField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
class IPMT_Form_model (models.Model):
    syllabus_Accomplished = models.IntegerField(null = True, blank = True)
    CourseGuide_Accomplished = models.IntegerField(null = True, blank = True)
    SLM_Accomplished = models.IntegerField(null = True, blank = True)
    SubjectAreas_Accomplished = models.IntegerField(null = True, blank = True)
    AttendanceSheet_Accomplished = models.IntegerField(null = True, blank = True)
    ClassRecord_Accomplished = models.IntegerField(null = True, blank = True)
    TeachingEffectiveness_Accomplished = models.IntegerField(null = True, blank = True)
    ClassroomObservation_Accomplished = models.IntegerField(null = True, blank = True)
    MidtermTOSRubrics_Accomplished = models.IntegerField(null = True, blank = True)
    FinaltermTOSRubrics_Accomplished = models.IntegerField(null = True, blank = True)
    MidtermTestQuestions_Accomplished = models.IntegerField(null = True, blank = True)
    FinaltermTestQuestions_Accomplished = models.IntegerField(null = True, blank = True)
    MidtermAnswerKey_Accomplished = models.IntegerField(null = True, blank = True)
    FinaltermAnswerKey_Accomplished = models.IntegerField(null = True, blank = True)
    GradingSheet_Accomplished = models.IntegerField(null = True, blank = True)
    StudentAdviced_Accomplished = models.IntegerField(null = True, blank = True)
    AccomplishmentReport_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchProposalSubmitted_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchImplemented_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchPresented_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchPublished_Accomplished = models.IntegerField(null = True, blank = True)
    ApprovedIPRights_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchUtilized_Accomplished = models.IntegerField(null = True, blank = True)
    NumberOfCitations_Accomplished = models.IntegerField(null = True, blank = True)
    ExtensionProposalSubmitted_Accomplished = models.IntegerField(null = True, blank = True)
    PersonTrained_Accomplished = models.IntegerField(null = True, blank = True)
    PersonAvailedRatedGood_Accomplished = models.IntegerField(null = True, blank = True)
    PersonTrainedRatedGood_Accomplished = models.IntegerField(null = True, blank = True)
    TechnicalAdvice_Accomplished = models.IntegerField(null = True, blank = True)
    AccomplishmentReportDeligatedAssignment_Accomplished = models.IntegerField(null = True, blank = True)
    FlagRaisingAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    FlagLoweringAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    WellnessProgramAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    SchoolCelebrationAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    TrainingAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    FacultyMeetingAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    AccreditationAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    SpiritualActivityAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    
    IPCR_Saved = models.DateField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)