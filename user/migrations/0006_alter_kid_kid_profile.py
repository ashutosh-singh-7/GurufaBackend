# Generated by Django 4.2.1 on 2023-07-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_kid_batch_enrolled_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='kid_profile',
            field=models.ImageField(blank=True, null=True, upload_to='images/users/'),
        ),
    ]
