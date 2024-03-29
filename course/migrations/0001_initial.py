# Generated by Django 4.2.1 on 2023-09-11 10:56

import course.models
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200, verbose_name='Course Name')),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True, verbose_name='Slug')),
                ('overview', models.TextField(blank=True, null=True, verbose_name='Course Overview')),
                ('about_guru', models.TextField(blank=True, null=True, verbose_name='About Guru')),
                ('course_icon', models.ImageField(upload_to='images/courses/', validators=[course.models.validate_course_icon_size])),
                ('course_banner', models.ImageField(upload_to='images/courses/', validators=[course.models.validate_course_banner_size])),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCourse',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200, verbose_name='Course Name')),
                ('slug', models.SlugField(editable=False, max_length=200, verbose_name='Slug')),
                ('overview', models.TextField(blank=True, null=True, verbose_name='Course Overview')),
                ('about_guru', models.TextField(blank=True, null=True, verbose_name='About Guru')),
                ('course_icon', models.TextField(max_length=100, validators=[course.models.validate_course_icon_size])),
                ('course_banner', models.TextField(max_length=100, validators=[course.models.validate_course_banner_size])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Course',
                'verbose_name_plural': 'historical Courses',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLevels',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100, verbose_name='Level Name')),
                ('description', models.CharField(default='Every Grandmaster Was A Novice.', max_length=100, verbose_name='Level Description')),
                ('num_classes', models.IntegerField(blank=True, null=True, verbose_name='Number Of Classes')),
                ('frequency', models.IntegerField(blank=True, null=True, verbose_name='Frequency (days/week)')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='Duration of course (in weeks)')),
                ('starts_from', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Starts From')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Course Level',
                'verbose_name_plural': 'historical Course Levels',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPlans',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(choices=[('One-on-One', 'One-on-One'), ('Batch', 'Batch'), ('Siblings', 'Siblings'), ('Demo Class', 'Demo Class')], max_length=100, verbose_name='Plan Name')),
                ('slug', models.SlugField(editable=False, max_length=200, verbose_name='Slug')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Plan Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Discont per cent')),
                ('is_active', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Course Plans',
                'verbose_name_plural': 'historical Course Plans',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSchedule',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('schedule_name', models.CharField(max_length=100, verbose_name='Schedule Name')),
                ('total_num_of_seats', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Total Number of seats')),
                ('seats_occupied', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Number of seats occupied')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Schedule',
                'verbose_name_plural': 'historical Schedules',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalScheduleTiming',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time ')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Session',
                'verbose_name_plural': 'historical Sessions',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100, verbose_name='Level Name')),
                ('description', models.CharField(default='Every Grandmaster Was A Novice.', max_length=100, verbose_name='Level Description')),
                ('num_classes', models.IntegerField(blank=True, null=True, verbose_name='Number Of Classes')),
                ('frequency', models.IntegerField(blank=True, null=True, verbose_name='Frequency (days/week)')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='Duration of course (in weeks)')),
                ('starts_from', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Starts From')),
            ],
            options={
                'verbose_name': 'Course Level',
                'verbose_name_plural': 'Course Levels',
            },
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('One-on-One', 'One-on-One'), ('Batch', 'Batch'), ('Siblings', 'Siblings'), ('Demo Class', 'Demo Class')], max_length=100, verbose_name='Plan Name')),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True, verbose_name='Slug')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Plan Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Discont per cent')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Course Plans',
                'verbose_name_plural': 'Course Plans',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('schedule_name', models.CharField(max_length=100, verbose_name='Schedule Name')),
                ('total_num_of_seats', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Total Number of seats')),
                ('seats_occupied', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Number of seats occupied')),
            ],
            options={
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedules',
            },
        ),
        migrations.CreateModel(
            name='ScheduleTiming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time ')),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timing', to='course.schedule')),
            ],
            options={
                'verbose_name': 'Session',
                'verbose_name_plural': 'Sessions',
            },
        ),
    ]
