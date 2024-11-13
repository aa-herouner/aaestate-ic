# Generated by Django 5.1 on 2024-10-17 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0005_alter_paymentsinformation_class_type_and_more'),
        ('students', '0010_alter_studentinfo_class_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentsinformation',
            name='class_type',
            field=models.ForeignKey(default='default_class', on_delete=django.db.models.deletion.CASCADE, to='students.studentclassinfo'),
        ),
        migrations.AlterField(
            model_name='paymentsinformation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]