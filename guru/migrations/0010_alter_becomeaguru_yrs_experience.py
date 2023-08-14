# Generated by Django 4.2.1 on 2023-08-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guru', '0009_alter_becomeaguru_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='becomeaguru',
            name='yrs_experience',
            field=models.CharField(choices=[('0 Years', '0 Years'), ('1-3 Years', '1-3 Years'), ('More than 3 years', 'More than 3 years')], max_length=50, verbose_name='Years of teaching experience'),
        ),
    ]
