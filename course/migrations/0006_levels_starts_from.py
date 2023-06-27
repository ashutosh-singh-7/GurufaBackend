# Generated by Django 4.2.1 on 2023-06-27 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_course_options_alter_levels_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='levels',
            name='starts_from',
            field=models.DecimalField(decimal_places=2, default=80, max_digits=10, verbose_name='Starts From'),
            preserve_default=False,
        ),
    ]
