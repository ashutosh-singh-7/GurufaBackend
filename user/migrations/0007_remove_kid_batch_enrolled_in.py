# Generated by Django 4.2.1 on 2023-07-01 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_kid_kid_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kid',
            name='batch_enrolled_in',
        ),
    ]
