# Generated by Django 3.1.7 on 2021-03-18 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sCode', models.CharField(max_length=250)),
                ('sRStatus', models.CharField(max_length=250)),
                ('sDescription', models.CharField(max_length=250)),
                ('sQuantity', models.IntegerField()),
            ],
        ),
    ]
