# Generated by Django 4.2.1 on 2023-09-11 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchase', '0001_initial'),
        ('course', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasesession',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchase',
            name='course_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.levels', verbose_name='Course Level Selected'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='kids_selected',
            field=models.ManyToManyField(blank=True, related_name='my_purchases', to='user.kid'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='plan_selected',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.plans', verbose_name='Plan Selected'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.schedule', verbose_name='Batch Enrolled in'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_purchase', to=settings.AUTH_USER_MODEL, verbose_name='Purchased By'),
        ),
        migrations.AddField(
            model_name='historicalpurchase',
            name='course_level',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course.levels', verbose_name='Course Level Selected'),
        ),
        migrations.AddField(
            model_name='historicalpurchase',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalpurchase',
            name='plan_selected',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course.plans', verbose_name='Plan Selected'),
        ),
        migrations.AddField(
            model_name='historicalpurchase',
            name='schedule',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course.schedule', verbose_name='Batch Enrolled in'),
        ),
        migrations.AddField(
            model_name='historicalpurchase',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Purchased By'),
        ),
    ]
