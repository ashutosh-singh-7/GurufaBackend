# Generated by Django 4.2.1 on 2023-06-29 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummy', models.JSONField(verbose_name='Dummy')),
            ],
        ),
    ]
