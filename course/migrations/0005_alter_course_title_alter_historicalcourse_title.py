# Generated by Django 4.2.1 on 2023-09-11 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_title_historicalcourse_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Course Title'),
        ),
        migrations.AlterField(
            model_name='historicalcourse',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Course Title'),
        ),
    ]
