# Generated by Django 4.1.2 on 2022-10-20 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_portal', '0006_remove_userdetails_company_remove_userdetails_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='recruiter_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=5, null=True)),
                ('type', models.CharField(max_length=15, null=True)),
                ('company', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
