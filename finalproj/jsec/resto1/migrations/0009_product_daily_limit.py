# Generated by Django 5.2.4 on 2025-07-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto1', '0008_remove_product_daily_limit_productlimit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='daily_limit',
            field=models.IntegerField(default=0),
        ),
    ]
