# Generated by Django 4.2.1 on 2023-06-28 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_course_course_banner'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faqs',
            options={'verbose_name': 'FAQ', 'verbose_name_plural': 'FAQs'},
        ),
        migrations.AddField(
            model_name='faqs',
            name='faq_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.course', verbose_name='FAQ For'),
        ),
        migrations.AlterField(
            model_name='faqs',
            name='answer',
            field=models.TextField(verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='faqs',
            name='question',
            field=models.CharField(max_length=200, verbose_name='Question'),
        ),
    ]
