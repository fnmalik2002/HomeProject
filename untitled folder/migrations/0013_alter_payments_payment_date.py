# Generated by Django 4.0 on 2022-01-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_rename_payment_uid_payments_payment_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='payment date'),
        ),
    ]
