# Generated by Django 4.2.1 on 2023-08-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_schedule_to_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
