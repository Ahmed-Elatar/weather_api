# Generated by Django 5.0.8 on 2024-08-10 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_location_name_weatherdata_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='localtime',
        ),
        migrations.RemoveField(
            model_name='weatherdata',
            name='localtime_epoch',
        ),
    ]
