# Generated by Django 4.2.1 on 2023-06-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_plans_to_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='slug',
            field=models.SlugField(default='One-on-one', editable=False, max_length=200, unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
