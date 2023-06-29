# Generated by Django 4.2.1 on 2023-06-27 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_batchtiming_batch_alter_batchtiming_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='batch_name',
            field=models.CharField(default='Batch 1', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='batchtiming',
            name='end_time',
            field=models.TimeField(verbose_name='End Time '),
        ),
    ]
