# Generated by Django 3.1.6 on 2021-04-19 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_attendnce_tracker'),
    ]

    operations = [
        migrations.DeleteModel(
            name='attendnce_tracker',
        ),
        migrations.RenameField(
            model_name='mark_attendance_manual',
            old_name='time',
            new_name='inTime',
        ),
        migrations.AddField(
            model_name='mark_attendance_manual',
            name='outTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]