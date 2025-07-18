# Generated by Django 5.2.4 on 2025-07-18 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto1', '0002_cartitem_refno_lineitem_refno_lineitem_storename_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'Cash'), ('online', 'Online')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='pickup_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='pickup_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_ref',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
