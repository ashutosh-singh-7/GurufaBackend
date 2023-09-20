# Generated by Django 4.2.1 on 2023-09-11 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
        ('course', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_reviews', to=settings.AUTH_USER_MODEL, verbose_name='Review given by'),
        ),
        migrations.AddField(
            model_name='review',
            name='to_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_reviews', to='course.course', verbose_name='Course'),
        ),
        migrations.AddField(
            model_name='historicalreview',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalreview',
            name='review_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Review given by'),
        ),
        migrations.AddField(
            model_name='historicalreview',
            name='to_course',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course.course', verbose_name='Course'),
        ),
        migrations.AddField(
            model_name='historicalfaqs',
            name='faq_for',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course.course', verbose_name='FAQ For'),
        ),
        migrations.AddField(
            model_name='historicalfaqs',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='faqs',
            name='faq_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_faqs', to='course.course', verbose_name='FAQ For'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('review_by', 'to_course')},
        ),
    ]