# Generated by Django 4.1.2 on 2022-10-20 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0005_userdetails_company_userdetails_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='company',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='status',
        ),
    ]
