# Generated by Django 3.1.6 on 2021-03-29 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing1', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=200)),
                ('nic', models.CharField(max_length=10)),
            ],
        ),
    ]
