# Generated by Django 5.2.4 on 2025-07-18 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resto1', '0010_remove_product_daily_limit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineitem',
            name='refno',
        ),
    ]
