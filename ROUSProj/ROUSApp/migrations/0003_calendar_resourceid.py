# Generated by Django 4.2.2 on 2023-07-07 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ROUSApp', '0002_remove_calendar_aircraft_calendar_mds_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='ResourceID',
            field=models.IntegerField(default=0),
        ),
    ]