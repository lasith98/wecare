# Generated by Django 3.1.6 on 2021-02-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_system', '0004_nursingofficer_nf_moh_reg_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nursingofficer',
            name='nf_moh_reg_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
