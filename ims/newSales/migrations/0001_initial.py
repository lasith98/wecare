# Generated by Django 3.1.7 on 2021-03-22 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('RStatus', models.CharField(max_length=250)),
            ],
        ),
    ]