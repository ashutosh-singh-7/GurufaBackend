# Generated by Django 4.2.1 on 2023-06-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_plans_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='count_sibling',
            field=models.BooleanField(default=False, verbose_name='Count Number of Siblings or Not?'),
        ),
    ]
