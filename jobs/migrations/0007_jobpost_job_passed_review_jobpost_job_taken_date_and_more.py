# Generated by Django 4.0 on 2021-12-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_jobpost_job_creator_alter_jobpost_job_taker'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='job_passed_review',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='job_taken_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date job taken'),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='job_under_review',
            field=models.BooleanField(default=False),
        ),
    ]
