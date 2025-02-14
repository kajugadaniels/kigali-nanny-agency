# Generated by Django 5.0.4 on 2025-02-14 16:34

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('child_care', 'Child Care'), ('elderly_care', 'Elderly Care'), ('sick_care', 'Sick Care'), ('disability_care', 'Disability Care'), ('housekeeping', 'Housekeeping'), ('pet_care', 'Pet Care'), ('nanny_share', 'Nanny Share'), ('house_nanny', 'House Nanny'), ('live_in_nanny', 'Live-in Nanny'), ('night_nanny', 'Night Nanny'), ('special_needs_care', 'Special Needs Care'), ('senior_care', 'Senior Care')], max_length=50)),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed'), ('pending', 'Pending'), ('in_progress', 'In Progress')], default='open', max_length=50)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('location', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_postings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Job Posting',
                'verbose_name_plural': 'Job Postings',
            },
        ),
    ]
