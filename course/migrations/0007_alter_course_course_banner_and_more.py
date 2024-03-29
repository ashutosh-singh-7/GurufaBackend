# Generated by Django 4.2.1 on 2023-09-11 11:22

import course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_course_course_banner_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_banner',
            field=models.ImageField(blank=True, null=True, upload_to='images/courses/', validators=[course.models.validate_course_banner_size]),
        ),
        migrations.AlterField(
            model_name='historicalcourse',
            name='course_banner',
            field=models.TextField(blank=True, max_length=100, null=True, validators=[course.models.validate_course_banner_size]),
        ),
    ]
