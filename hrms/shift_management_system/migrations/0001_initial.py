# Generated by Django 3.1.6 on 2021-02-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_date', models.DateField()),
                ('s_start', models.IntegerField()),
                ('s_end', models.IntegerField()),
                ('s_month', models.CharField(choices=[('January', 'january'), ('February', 'february'), ('March', 'march'), ('April', 'april'), ('May', 'may'), ('June', 'june'), ('July', 'july'), ('August', 'august'), ('September', 'september'), ('October', 'october'), ('November', 'november'), ('December', 'december')], max_length=200, null=True)),
            ],
        ),
    ]
