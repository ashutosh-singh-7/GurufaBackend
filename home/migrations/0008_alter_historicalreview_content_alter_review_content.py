# Generated by Django 4.2.1 on 2023-09-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_historicalreview_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalreview',
            name='content',
            field=models.TextField(max_length=200, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(max_length=200, verbose_name='Content'),
        ),
    ]