# Generated by Django 5.2.4 on 2025-07-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto1', '0011_remove_lineitem_refno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='storename',
            field=models.CharField(default="Sip 'n' Scoop"),
        ),
    ]
