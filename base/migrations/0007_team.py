# Generated by Django 5.0.4 on 2025-03-12 11:03

import base.models
import imagekit.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=base.models.team_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Team Members',
            },
        ),
    ]
