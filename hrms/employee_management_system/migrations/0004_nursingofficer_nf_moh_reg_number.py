# Generated by Django 3.1.6 on 2021-02-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_system', '0003_auto_20210226_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='nursingofficer',
            name='nf_moh_reg_number',
            field=models.CharField(default=0, max_length=20, unique=True),
        ),
    ]