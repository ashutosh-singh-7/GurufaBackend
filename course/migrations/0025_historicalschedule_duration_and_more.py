# Generated by Django 4.2.1 on 2023-10-01 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0024_alter_historicallevels_num_classes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalschedule',
            name='duration',
            field=models.IntegerField(blank=True, null=True, verbose_name='Duration of course (in weeks)'),
        ),
        migrations.AddField(
            model_name='historicalschedule',
            name='frequency',
            field=models.IntegerField(blank=True, null=True, verbose_name='Frequency (days/week)'),
        ),
        migrations.AddField(
            model_name='historicalschedule',
            name='num_classes',
            field=models.IntegerField(blank=True, help_text='Leave blank if it should be calculated via frequency and duration.', null=True, verbose_name='Number Of Classes/Sessions'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='duration',
            field=models.IntegerField(blank=True, null=True, verbose_name='Duration of course (in weeks)'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='frequency',
            field=models.IntegerField(blank=True, null=True, verbose_name='Frequency (days/week)'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='num_classes',
            field=models.IntegerField(blank=True, help_text='Leave blank if it should be calculated via frequency and duration.', null=True, verbose_name='Number Of Classes/Sessions'),
        ),
        migrations.AlterField(
            model_name='historicallevels',
            name='num_classes',
            field=models.IntegerField(blank=True, help_text='Leave blank if it should be calculated via frequency and duration.', null=True, verbose_name='Number Of Classes/Sessions'),
        ),
        migrations.AlterField(
            model_name='levels',
            name='num_classes',
            field=models.IntegerField(blank=True, help_text='Leave blank if it should be calculated via frequency and duration.', null=True, verbose_name='Number Of Classes/Sessions'),
        ),
    ]
