# Generated by Django 4.1.7 on 2023-06-02 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0039_remove_ipcr_form_model_approver_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPMT_Form_model_submitted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus_Accomplished', models.IntegerField(blank=True, null=True)),
                ('CourseGuide_Accomplished', models.IntegerField(blank=True, null=True)),
                ('SLM_Accomplished', models.IntegerField(blank=True, null=True)),
                ('SubjectAreas_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AttendanceSheet_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ClassRecord_Accomplished', models.IntegerField(blank=True, null=True)),
                ('TeachingEffectiveness_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ClassroomObservation_Accomplished', models.IntegerField(blank=True, null=True)),
                ('TOSRubrics_Accomplished', models.IntegerField(blank=True, null=True)),
                ('TestQuestions_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AnswerKey_Accomplished', models.IntegerField(blank=True, null=True)),
                ('GradingSheet_Accomplished', models.IntegerField(blank=True, null=True)),
                ('StudentAdviced_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AccomplishmentReport_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchProposalSubmitted_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchImplemented_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchPresented_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchPublished_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ApprovedIPRights_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchUtilized_Accomplished', models.IntegerField(blank=True, null=True)),
                ('NumberOfCitations_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ExtensionProposalSubmitted_Accomplished', models.IntegerField(blank=True, null=True)),
                ('PersonTrained_Accomplished', models.IntegerField(blank=True, null=True)),
                ('PersonAvailedRatedGood_Accomplished', models.IntegerField(blank=True, null=True)),
                ('PersonTrainedRatedGood_Accomplished', models.IntegerField(blank=True, null=True)),
                ('TechnicalAdvice_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AccomplishmentReportDeligatedAssignment_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FlagRaisingAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FlagLoweringAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('WellnessProgramAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('SchoolCelebrationAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('TrainingAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FacultyMeetingAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AccreditationAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('SpiritualActivityAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('IPCR_Saved', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]