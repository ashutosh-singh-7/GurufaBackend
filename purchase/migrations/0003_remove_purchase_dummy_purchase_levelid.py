# Generated by Django 4.2.1 on 2023-06-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_alter_purchase_options_alter_purchase_dummy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='dummy',
        ),
        migrations.AddField(
            model_name='purchase',
            name='levelID',
            field=models.IntegerField(blank=True, null=True, verbose_name='Level ID'),
        ),
    ]
