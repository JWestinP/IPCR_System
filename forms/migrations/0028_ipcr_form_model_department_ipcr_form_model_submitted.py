# Generated by Django 4.1.7 on 2023-05-27 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0027_rename_midtermanswerkey_accomplished_ipmt_form_model_answerkey_accomplished_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipcr_form_model',
            name='department',
            field=models.ManyToManyField(null=True, to='auth.group'),
        ),
        migrations.CreateModel(
            name='IPCR_Form_model_submitted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('syllabus_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('CourseGuide_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('CourseGuide_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('SLM_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('SLM_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('SubjectAreas_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('SubjectAreas_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('AttendanceSheet_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('AttendanceSheet_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('ClassRecord_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('ClassRecord_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('TeachingEffectiveness_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('TeachingEffectiveness_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('ClassroomObservation_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('ClassroomObservation_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('MidtermTOSRubrics_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('MidtermTOSRubrics_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('FinaltermTOSRubrics_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('FinaltermTOSRubrics_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('MidtermTestQuestions_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('MidtermTestQuestions_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('FinaltermTestQuestions_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('FinaltermTestQuestions_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('MidtermAnswerKey_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('MidtermAnswerKey_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('FinaltermAnswerKey_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('FinaltermAnswerKey_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('GradingSheet_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('GradingSheet_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('StudentAdviced_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('StudentAdviced_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('AccomplishmentReport_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('AccomplishmentReport_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('ResearchProposalSubmitted_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('ResearchProposalSubmitted_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('ResearchImplemented_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('ResearchImplemented_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('ResearchPresented_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('ResearchPresented_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('ResearchPublished_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('ResearchPublished_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('ApprovedIPRights_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('ApprovedIPRights_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('ResearchUtilized_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('ResearchUtilized_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('NumberOfCitations_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('NumberOfCitations_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('ExtensionProposalSubmitted_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('ExtensionProposalSubmitted_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('PersonTrained_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('PersonTrained_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('PersonAvailedRatedGood_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('PersonAvailedRatedGood_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('PersonTrainedRatedGood_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('PersonTrainedRatedGood_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('TechnicalAdvice_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('TechnicalAdvice_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('AccomplishmentReportDeligatedAssignment_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('AccomplishmentReportDeligatedAssignment_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('FlagRaisingAttendance_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('FlagRaisingAttendance_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('FlagLoweringAttendance_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('FlagLoweringAttendance_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('WellnessProgramAttendance_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('WellnessProgramAttendance_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('SchoolCelebrationAttendance_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('SchoolCelebrationAttendance_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('TrainingAttendance_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('TrainingAttendance_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('FacultyMeetingAttendance_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('FacultyMeetingAttendance_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('AccreditationAttendance_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('AccreditationAttendance_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('SpiritualActivityAttendance_Target', models.IntegerField(blank=True, default=0, null=True)),
                ('SpiritualActivityAttendance_Accomplished', models.IntegerField(blank=True, default=0, null=True)),
                ('IPCR_Deadline', models.DateField(blank=True, null=True)),
                ('IPCR_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]