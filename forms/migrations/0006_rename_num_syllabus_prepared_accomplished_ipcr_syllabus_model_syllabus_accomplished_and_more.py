# Generated by Django 4.1.7 on 2023-05-04 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_rename_ipcr_ipcr_syllabus_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipcr_syllabus_model',
            old_name='Num_syllabus_prepared_Accomplished',
            new_name='syllabus_Accomplished',
        ),
        migrations.RenameField(
            model_name='ipcr_syllabus_model',
            old_name='Num_syllabus_prepared_Target',
            new_name='syllabus_Target',
        ),
    ]
