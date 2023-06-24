# Generated by Django 4.2.1 on 2023-06-22 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_course_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=None, editable=False, max_length=200, unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
