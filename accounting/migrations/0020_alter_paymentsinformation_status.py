# Generated by Django 5.1 on 2024-10-22 19:55

import accounting.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0019_paymentstatus_paymentsinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentsinformation',
            name='status',
            field=models.CharField(max_length=20, verbose_name=accounting.models.PaymentStatus),
        ),
    ]