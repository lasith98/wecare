# Generated by Django 3.1.6 on 2021-04-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thyrod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tstBox1', models.CharField(max_length=250)),
                ('tstBox2', models.CharField(max_length=250)),
                ('tstBox3', models.CharField(max_length=250)),
                ('tstBox4', models.CharField(max_length=250)),
                ('resultBox1', models.CharField(max_length=250)),
                ('resultBox2', models.CharField(max_length=250)),
                ('resultBox3', models.CharField(max_length=250)),
                ('resultBox4', models.CharField(max_length=250)),
                ('normalBox1', models.CharField(max_length=250)),
                ('normalBox2', models.CharField(max_length=250)),
                ('normalBox3', models.CharField(max_length=250)),
                ('normalBox4', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
