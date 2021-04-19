# Generated by Django 3.1.6 on 2021-04-15 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinical', '0002_labreport_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labreport',
            name='status',
            field=models.CharField(choices=[('Ready to send lab', 'Ready To Send Lab'), ('Queue', 'In Queue'), ('Start Processing', 'Start Processing'), ('Complete', 'Completed')], default='Ready to send lab', max_length=20),
        ),
    ]
