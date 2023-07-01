# Generated by Django 4.2.1 on 2023-06-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_remove_purchase_dummy_purchase_levelid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='levelID',
        ),
        migrations.AddField(
            model_name='purchase',
            name='dummy',
            field=models.JSONField(blank=True, null=True, verbose_name='Dummy'),
        ),
    ]
