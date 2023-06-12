# Generated by Django 4.2.2 on 2023-06-12 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ROUSApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Aircraft', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('EHours', models.FloatField(blank=True, default=0.0, null=True)),
                ('FHours', models.FloatField(blank=True, default=0.0, null=True)),
                ('GeoLoc', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Calender',
        ),
        migrations.AddField(
            model_name='partmaintenance',
            name='DueDate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='planemaintenance',
            name='CrntTime',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='planemaintenance',
            name='DueDate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='planemaintenance',
            name='DueTime',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='planemaintenance',
            name='TimeRemain',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]