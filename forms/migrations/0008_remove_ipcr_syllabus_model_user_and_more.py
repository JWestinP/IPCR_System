# Generated by Django 4.1.7 on 2023-05-04 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0007_ipcr_syllabus_model_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipcr_syllabus_model',
            name='user',
        ),
        migrations.AddField(
            model_name='ipcr_syllabus_model',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
