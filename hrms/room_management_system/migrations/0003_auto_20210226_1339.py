# Generated by Django 3.1.6 on 2021-02-26 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_system', '0001_initial'),
        ('room_management_system', '0002_allocationtable_d_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocationtable',
            name='d_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_system.doctor'),
        ),
    ]
