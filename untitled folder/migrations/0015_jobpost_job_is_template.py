# Generated by Django 4.0 on 2022-01-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_payments_payment_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='job_is_template',
            field=models.BooleanField(default=False),
        ),
    ]
