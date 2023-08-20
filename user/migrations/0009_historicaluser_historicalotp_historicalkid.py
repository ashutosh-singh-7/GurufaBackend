# Generated by Django 4.2.1 on 2023-08-20 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import simple_history.models
import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_kid_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('picture', models.TextField(blank=True, max_length=100, null=True)),
                ('auth_provider_img', models.URLField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')),
                ('auth_providers', models.CharField(choices=[('Email', 'AUTH_PROVIDER_EMAIL'), ('Google', 'AUTH_PROVIDER_GOOGLE')], default='Email', max_length=100, verbose_name='Auth Providers')),
                ('user_roles', models.CharField(choices=[('Parent', 'PARENT'), ('Guru', 'GURU')], default='Parent', max_length=100, verbose_name='User Role')),
                ('is_a_guru', models.BooleanField(default=False, verbose_name='Is A Guru?')),
                ('first_name', models.CharField(max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last name')),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='Email address')),
                ('is_email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone Number ')),
                ('is_phone_verified', models.BooleanField(default=False, verbose_name='Phone verified')),
                ('whatsapp_update', models.BooleanField(default=False, verbose_name='Opted for WhatsApp Update')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical User',
                'verbose_name_plural': 'historical Users',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalOTP',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('otp_code', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical otp',
                'verbose_name_plural': 'historical otps',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalKid',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('kid_profile', models.TextField(blank=True, default='images/kids/kids_avatar.png', max_length=100, null=True, verbose_name="Kid's Profile Picture")),
                ('kid_gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Prefer Not to Answer/State', 'PNAS')], default='Prefer Not to Answer/State', max_length=100, verbose_name="Kid's Gender")),
                ('kid_first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('kid_last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('kid_age', models.PositiveIntegerField(default=5, validators=[user.validators.validate_kids_age], verbose_name="Kid's Age (In Years)")),
                ('is_active', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('kid_parent', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Kid',
                'verbose_name_plural': 'historical Kids',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
