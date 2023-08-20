# Generated by Django 4.2.1 on 2023-08-19 17:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0004_remove_plans_actual_price_and_more'),
        ('home', '0004_review_created_at'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('review_by', 'to_course')},
        ),
    ]