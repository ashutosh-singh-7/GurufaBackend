# Generated by Django 4.2.1 on 2023-07-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0010_rename_batch_purchase_schedule_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='payment_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('FAILED', 'Failed')], default='PENDING', max_length=10, verbose_name='Payment Status'),
        ),
    ]