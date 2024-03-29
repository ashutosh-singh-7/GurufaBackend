# Generated by Django 4.2.1 on 2023-09-24 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_rename_historicalscheduletiming_historicalsession_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalschedule',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='historicalschedule',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='historicalschedule',
            name='num_classes',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='num_classes',
        ),
        migrations.AddField(
            model_name='historicallevels',
            name='duration',
            field=models.IntegerField(blank=True, null=True, verbose_name='Duration of course (in weeks)'),
        ),
        migrations.AddField(
            model_name='historicallevels',
            name='frequency',
            field=models.IntegerField(blank=True, null=True, verbose_name='Frequency (days/week)'),
        ),
        migrations.AddField(
            model_name='historicallevels',
            name='num_classes',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number Of Classes'),
        ),
        migrations.AddField(
            model_name='levels',
            name='duration',
            field=models.IntegerField(blank=True, null=True, verbose_name='Duration of course (in weeks)'),
        ),
        migrations.AddField(
            model_name='levels',
            name='frequency',
            field=models.IntegerField(blank=True, null=True, verbose_name='Frequency (days/week)'),
        ),
        migrations.AddField(
            model_name='levels',
            name='num_classes',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number Of Classes'),
        ),
    ]
