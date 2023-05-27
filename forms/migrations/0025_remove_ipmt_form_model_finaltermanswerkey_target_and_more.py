# Generated by Django 4.1.7 on 2023-05-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0024_ipmt_form_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipmt_form_model',
            name='FinaltermAnswerKey_Target',
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='AccomplishmentReportDeligatedAssignment_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='AccomplishmentReportDeligatedAssignment_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='AccomplishmentReport_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='AccomplishmentReport_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='AccreditationAttendance_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='AccreditationAttendance_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ApprovedIPRights_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ApprovedIPRights_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='AttendanceSheet_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='AttendanceSheet_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ClassRecord_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ClassRecord_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ClassroomObservation_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ClassroomObservation_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='CourseGuide_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='CourseGuide_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ExtensionProposalSubmitted_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ExtensionProposalSubmitted_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='FacultyMeetingAttendance_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='FacultyMeetingAttendance_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='FinaltermAnswerKey_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='FinaltermAnswerKey_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='FinaltermTOSRubrics_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='FinaltermTOSRubrics_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='FinaltermTestQuestions_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='FinaltermTestQuestions_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='FlagLoweringAttendance_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='FlagLoweringAttendance_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='FlagRaisingAttendance_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='FlagRaisingAttendance_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='GradingSheet_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='GradingSheet_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='MidtermAnswerKey_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='MidtermAnswerKey_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='MidtermTOSRubrics_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='MidtermTOSRubrics_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='MidtermTestQuestions_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='MidtermTestQuestions_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='NumberOfCitations_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='NumberOfCitations_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='PersonAvailedRatedGood_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='PersonAvailedRatedGood_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='PersonTrainedRatedGood_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='PersonTrainedRatedGood_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='PersonTrained_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='PersonTrained_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ResearchImplemented_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ResearchImplemented_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ResearchPresented_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ResearchPresented_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ResearchProposalSubmitted_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ResearchProposalSubmitted_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ResearchPublished_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ResearchPublished_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ResearchUtilized_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='ResearchUtilized_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='SLM_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='SLM_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='SchoolCelebrationAttendance_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='SchoolCelebrationAttendance_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='SpiritualActivityAttendance_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='SpiritualActivityAttendance_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='StudentAdviced_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='StudentAdviced_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='SubjectAreas_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='SubjectAreas_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='TeachingEffectiveness_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='TeachingEffectiveness_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='TechnicalAdvice_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='TechnicalAdvice_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='TrainingAttendance_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='TrainingAttendance_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='WellnessProgramAttendance_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='WellnessProgramAttendance_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='syllabus_Accomplished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipcr_form_model',
            name='syllabus_Target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]