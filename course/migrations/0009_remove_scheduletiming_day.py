# Generated by Django 4.2.1 on 2023-08-20 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_scheduletiming_options_scheduletiming_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduletiming',
            name='day',
        ),
    ]