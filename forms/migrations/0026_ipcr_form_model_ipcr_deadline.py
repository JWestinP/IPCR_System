# Generated by Django 4.1.7 on 2023-05-27 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0025_remove_ipmt_form_model_finaltermanswerkey_target_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipcr_form_model',
            name='IPCR_Deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]