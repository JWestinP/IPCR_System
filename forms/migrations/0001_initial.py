# Generated by Django 4.1.7 on 2023-05-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPCR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_syllabus_prepared_Target', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
