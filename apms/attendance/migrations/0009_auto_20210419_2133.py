# Generated by Django 3.1.6 on 2021-04-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_auto_20210419_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark_attendance_manual',
            name='outTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]