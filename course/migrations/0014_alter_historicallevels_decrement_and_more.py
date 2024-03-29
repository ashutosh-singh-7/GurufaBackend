# Generated by Django 4.2.1 on 2023-09-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_remove_course_about_guru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallevels',
            name='decrement',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Decrease price by: '),
        ),
        migrations.AlterField(
            model_name='historicallevels',
            name='increment',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Increase price by: '),
        ),
        migrations.AlterField(
            model_name='historicalplans',
            name='discount_percent',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Discont per cent'),
        ),
        migrations.AlterField(
            model_name='levels',
            name='decrement',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Decrease price by: '),
        ),
        migrations.AlterField(
            model_name='levels',
            name='increment',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Increase price by: '),
        ),
        migrations.AlterField(
            model_name='plans',
            name='discount_percent',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Discont per cent'),
        ),
    ]
