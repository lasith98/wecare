# Generated by Django 3.1.7 on 2021-03-19 05:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bloodCount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodcount',
            name='resultBox1',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bloodcount',
            name='resultBox2',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bloodcount',
            name='resultBox3',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bloodcount',
            name='resultBox4',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
