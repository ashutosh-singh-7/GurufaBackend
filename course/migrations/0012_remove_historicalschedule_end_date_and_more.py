# Generated by Django 4.2.1 on 2023-08-31 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_historicalplans_discount_percent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalschedule',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='historicalschedule',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='start_date',
        ),
    ]
