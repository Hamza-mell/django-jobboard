# Generated by Django 5.1.6 on 2025-03-04 15:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default=1, max_length=1000),
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full time', 'Full time'), ('Part time', 'Part time')], default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]
