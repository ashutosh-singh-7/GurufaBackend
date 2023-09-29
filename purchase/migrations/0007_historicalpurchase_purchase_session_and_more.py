# Generated by Django 4.2.1 on 2023-09-26 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0006_alter_purchase_course_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpurchase',
            name='purchase_session',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='purchase.purchasesession'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchase_session',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase', to='purchase.purchasesession'),
        ),
    ]