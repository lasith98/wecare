# Generated by Django 3.1.7 on 2021-03-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20210317_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='supplier',
            field=models.CharField(max_length=260),
        ),
    ]
