# Generated by Django 3.1.7 on 2021-03-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='purchase',
            field=models.IntegerField(max_length=250),
        ),
        migrations.AlterField(
            model_name='items',
            name='unitPrice',
            field=models.IntegerField(max_length=250),
        ),
    ]
