# Generated by Django 4.2.1 on 2023-09-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_alter_schedule_guru'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallevels',
            name='decrement',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True, verbose_name='Decrease price by: '),
        ),
        migrations.AlterField(
            model_name='historicallevels',
            name='increment',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True, verbose_name='Increase price by: '),
        ),
        migrations.AlterField(
            model_name='historicalschedule',
            name='schedule_name',
            field=models.CharField(blank=True, help_text='Leave blank to automaticallly assign a name.', max_length=100, null=True, verbose_name='Schedule Name'),
        ),
        migrations.AlterField(
            model_name='levels',
            name='decrement',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True, verbose_name='Decrease price by: '),
        ),
        migrations.AlterField(
            model_name='levels',
            name='increment',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True, verbose_name='Increase price by: '),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='schedule_name',
            field=models.CharField(blank=True, help_text='Leave blank to automaticallly assign a name.', max_length=100, null=True, verbose_name='Schedule Name'),
        ),
    ]
