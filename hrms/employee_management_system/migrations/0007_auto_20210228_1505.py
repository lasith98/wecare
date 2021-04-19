# Generated by Django 3.1.6 on 2021-02-28 09:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_system', '0006_auto_20210228_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salarygroup',
            name='sg_basic_salary',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
