# Generated by Django 3.1.6 on 2021-02-26 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room_management_system', '0003_auto_20210226_1339'),
        ('employee_management_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nursingofficer',
            name='r_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='room_management_system.room'),
        ),
    ]
