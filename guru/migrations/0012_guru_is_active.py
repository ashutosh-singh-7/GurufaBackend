# Generated by Django 4.2.1 on 2023-08-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guru', '0011_alter_becomeaguru_yrs_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='guru',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
