# Generated by Django 4.1.7 on 2023-05-25 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0021_rename_ipcr_attendancesa_model_ipcr_spiritualactivityattendance_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPCR_Form_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus_Target', models.IntegerField(blank=True, null=True)),
                ('syllabus_Accomplished', models.IntegerField(blank=True, null=True)),
                ('CourseGuide_Target', models.IntegerField(blank=True, null=True)),
                ('CourseGuide_Accomplished', models.IntegerField(blank=True, null=True)),
                ('SLM_Target', models.IntegerField(blank=True, null=True)),
                ('SLM_Accomplished', models.IntegerField(blank=True, null=True)),
                ('SubjectAreas_Target', models.IntegerField(blank=True, null=True)),
                ('SubjectAreas_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AttendanceSheet_Target', models.IntegerField(blank=True, null=True)),
                ('AttendanceSheet_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ClassRecord_Target', models.IntegerField(blank=True, null=True)),
                ('ClassRecord_Accomplished', models.IntegerField(blank=True, null=True)),
                ('TeachingEffectiveness_Target', models.IntegerField(blank=True, null=True)),
                ('TeachingEffectiveness_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ClassroomObservation_Target', models.IntegerField(blank=True, null=True)),
                ('ClassroomObservation_Accomplished', models.IntegerField(blank=True, null=True)),
                ('MidtermTOSRubrics_Target', models.IntegerField(blank=True, null=True)),
                ('MidtermTOSRubrics_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FinaltermTOSRubrics_Target', models.IntegerField(blank=True, null=True)),
                ('FinaltermTOSRubrics_Accomplished', models.IntegerField(blank=True, null=True)),
                ('MidtermTestQuestions_Target', models.IntegerField(blank=True, null=True)),
                ('MidtermTestQuestions_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FinaltermTestQuestions_Target', models.IntegerField(blank=True, null=True)),
                ('FinaltermTestQuestions_Accomplished', models.IntegerField(blank=True, null=True)),
                ('MidtermAnswerKey_Target', models.IntegerField(blank=True, null=True)),
                ('MidtermAnswerKey_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FinaltermAnswerKey_Target', models.IntegerField(blank=True, null=True)),
                ('FinaltermAnswerKey_Accomplished', models.IntegerField(blank=True, null=True)),
                ('GradingSheet_Target', models.IntegerField(blank=True, null=True)),
                ('GradingSheet_Accomplished', models.IntegerField(blank=True, null=True)),
                ('StudentAdviced_Target', models.IntegerField(blank=True, null=True)),
                ('StudentAdviced_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AccomplishmentReport_Target', models.IntegerField(blank=True, null=True)),
                ('AccomplishmentReport_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchProposalSubmitted_Target', models.IntegerField(blank=True, null=True)),
                ('ResearchProposalSubmitted_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchImplemented_Target', models.IntegerField(blank=True, null=True)),
                ('ResearchImplemented_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchPresented_Target', models.IntegerField(blank=True, null=True)),
                ('ResearchPresented_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchPublished_Target', models.IntegerField(blank=True, null=True)),
                ('ResearchPublished_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ApprovedIPRights_Target', models.IntegerField(blank=True, null=True)),
                ('ApprovedIPRights_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchUtilized_Target', models.IntegerField(blank=True, null=True)),
                ('ResearchUtilized_Accomplished', models.IntegerField(blank=True, null=True)),
                ('NumberOfCitations_Target', models.IntegerField(blank=True, null=True)),
                ('NumberOfCitations_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ExtensionProposalSubmitted_Target', models.IntegerField(blank=True, null=True)),
                ('ExtensionProposalSubmitted_Accomplished', models.IntegerField(blank=True, null=True)),
                ('PersonTrained_Target', models.IntegerField(blank=True, null=True)),
                ('PersonTrained_Accomplished', models.IntegerField(blank=True, null=True)),
                ('PersonAvailedRatedGood_Target', models.IntegerField(blank=True, null=True)),
                ('PersonAvailedRatedGood_Accomplished', models.IntegerField(blank=True, null=True)),
                ('PersonTrainedRatedGood_Target', models.IntegerField(blank=True, null=True)),
                ('PersonTrainedRatedGood_Accomplished', models.IntegerField(blank=True, null=True)),
                ('TechnicalAdvice_Target', models.IntegerField(blank=True, null=True)),
                ('TechnicalAdvice_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AccomplishmentReportDeligatedAssignment_Target', models.IntegerField(blank=True, null=True)),
                ('AccomplishmentReportDeligatedAssignment_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FlagRaisingAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('FlagRaisingAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FlagLoweringAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('FlagLoweringAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('WellnessProgramAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('WellnessProgramAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('SchoolCelebrationAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('SchoolCelebrationAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('TrainingAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('TrainingAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FacultyMeetingAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('FacultyMeetingAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AccreditationAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('AccreditationAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('SpiritualActivityAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('SpiritualActivityAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='ipcr_accomplishmentreportdeligatedassignment_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_accreditationattendance_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_approvediprights_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_attendancesheet_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_classrecord_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_classroomobservation_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_courseguide_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_extensionproposalsubmitted_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_facultymeetingattendance_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_finaltermanswerkey_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_finaltermtestquestions_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_finaltermtosrubrics_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_flagloweringattendance_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_flagraisingattendance_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_gradingsheet_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_midtermanswerkey_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_midtermtestquestions_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_midtermtosrubrics_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_numberofcitations_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_personavailedratedgood_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_persontrained_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_persontrainedratedgood_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_researchimplemented_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_researchpresented_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_researchproposalsubmitted_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_researchpublished_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_researchutilized_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_schoolcelebrationattendance_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_slm_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_spiritualactivityattendance_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_studentadviced_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_subjectareas_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_syllabus_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_teachingeffectiveness_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_technicaladvice_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_trainingattendance_model',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ipcr_wellnessprogramattendance_model',
            name='author',
        ),
        migrations.DeleteModel(
            name='IPCR_AccomplishmentReport_model',
        ),
        migrations.DeleteModel(
            name='IPCR_AccomplishmentReportDeligatedAssignment_model',
        ),
        migrations.DeleteModel(
            name='IPCR_AccreditationAttendance_model',
        ),
        migrations.DeleteModel(
            name='IPCR_ApprovedIPRights_model',
        ),
        migrations.DeleteModel(
            name='IPCR_AttendanceSheet_model',
        ),
        migrations.DeleteModel(
            name='IPCR_ClassRecord_model',
        ),
        migrations.DeleteModel(
            name='IPCR_ClassroomObservation_model',
        ),
        migrations.DeleteModel(
            name='IPCR_CourseGuide_model',
        ),
        migrations.DeleteModel(
            name='IPCR_ExtensionProposalSubmitted_model',
        ),
        migrations.DeleteModel(
            name='IPCR_FacultyMeetingAttendance_model',
        ),
        migrations.DeleteModel(
            name='IPCR_FinaltermAnswerKey_model',
        ),
        migrations.DeleteModel(
            name='IPCR_FinaltermTestQuestions_model',
        ),
        migrations.DeleteModel(
            name='IPCR_FinaltermTOSRubrics_model',
        ),
        migrations.DeleteModel(
            name='IPCR_FlagLoweringAttendance_model',
        ),
        migrations.DeleteModel(
            name='IPCR_FlagRaisingAttendance_model',
        ),
        migrations.DeleteModel(
            name='IPCR_GradingSheet_model',
        ),
        migrations.DeleteModel(
            name='IPCR_MidtermAnswerKey_model',
        ),
        migrations.DeleteModel(
            name='IPCR_MidtermTestQuestions_model',
        ),
        migrations.DeleteModel(
            name='IPCR_MidtermTOSRubrics_model',
        ),
        migrations.DeleteModel(
            name='IPCR_NumberOfCitations_model',
        ),
        migrations.DeleteModel(
            name='IPCR_PersonAvailedRatedGood_model',
        ),
        migrations.DeleteModel(
            name='IPCR_PersonTrained_model',
        ),
        migrations.DeleteModel(
            name='IPCR_PersonTrainedRatedGood_model',
        ),
        migrations.DeleteModel(
            name='IPCR_ResearchImplemented_model',
        ),
        migrations.DeleteModel(
            name='IPCR_ResearchPresented_model',
        ),
        migrations.DeleteModel(
            name='IPCR_ResearchProposalSubmitted_model',
        ),
        migrations.DeleteModel(
            name='IPCR_ResearchPublished_model',
        ),
        migrations.DeleteModel(
            name='IPCR_ResearchUtilized_model',
        ),
        migrations.DeleteModel(
            name='IPCR_SchoolCelebrationAttendance_model',
        ),
        migrations.DeleteModel(
            name='IPCR_SLM_model',
        ),
        migrations.DeleteModel(
            name='IPCR_SpiritualActivityAttendance_model',
        ),
        migrations.DeleteModel(
            name='IPCR_StudentAdviced_model',
        ),
        migrations.DeleteModel(
            name='IPCR_SubjectAreas_model',
        ),
        migrations.DeleteModel(
            name='IPCR_Syllabus_model',
        ),
        migrations.DeleteModel(
            name='IPCR_TeachingEffectiveness_model',
        ),
        migrations.DeleteModel(
            name='IPCR_TechnicalAdvice_model',
        ),
        migrations.DeleteModel(
            name='IPCR_TrainingAttendance_model',
        ),
        migrations.DeleteModel(
            name='IPCR_WellnessProgramAttendance_model',
        ),
    ]