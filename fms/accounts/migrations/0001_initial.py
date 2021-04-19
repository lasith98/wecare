# Generated by Django 3.1.4 on 2021-04-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_no', models.CharField(max_length=20)),
                ('acc_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('bank_name', models.CharField(max_length=100)),
                ('branch_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('street_a1', models.CharField(max_length=100)),
                ('street_a2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
    ]
