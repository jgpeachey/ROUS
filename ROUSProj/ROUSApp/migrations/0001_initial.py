# Generated by Django 4.2.2 on 2023-07-23 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('CalendarID', models.AutoField(primary_key=True, serialize=False)),
                ('JulianDate', models.IntegerField(default=0)),
                ('MDS', models.CharField(max_length=10)),
                ('TailNumber', models.CharField(max_length=10)),
                ('title', models.TextField(blank=True)),
                ('EHours', models.FloatField(blank=True, default=0.0, null=True)),
                ('FHours', models.FloatField(blank=True, default=0.0, null=True)),
                ('GeoLoc', models.CharField(max_length=10)),
                ('PlaneMaintenanceID', models.IntegerField(default=0)),
                ('PartMaintenanceID', models.IntegerField(default=0)),
                ('ResourceID', models.IntegerField(default=0)),
                ('Completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('GeoLoc', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('ResourceID', models.AutoField(primary_key=True, serialize=False)),
                ('TailNumber', models.CharField(max_length=10)),
                ('GeoLoc', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PlaneMaintenance',
            fields=[
                ('PlaneMaintenanceID', models.AutoField(primary_key=True, serialize=False)),
                ('PlaneSN', models.CharField(max_length=10)),
                ('MDS', models.CharField(max_length=10)),
                ('Narrative', models.TextField(default='')),
                ('CrntTime', models.FloatField(blank=True, default=0.0, null=True)),
                ('TimeRemain', models.FloatField(blank=True, default=0.0, null=True)),
                ('DueTime', models.FloatField(blank=True, default=0.0, null=True)),
                ('Freq', models.SmallIntegerField(default=0)),
                ('Type', models.CharField(max_length=1)),
                ('JST', models.IntegerField(default=0)),
                ('TFrame', models.SmallIntegerField(default=0)),
                ('E_F', models.CharField(max_length=10)),
                ('title', models.TextField(blank=True)),
                ('Scheduled', models.BooleanField(default=False)),
            ],
            options={
                'unique_together': {('PlaneSN', 'MDS', 'title')},
            },
        ),
        migrations.CreateModel(
            name='PlaneData',
            fields=[
                ('PlaneSN', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('GeoLoc', models.CharField(max_length=10)),
                ('MDS', models.CharField(max_length=10)),
                ('TailNumber', models.CharField(max_length=10)),
            ],
            options={
                'unique_together': {('PlaneSN', 'MDS')},
            },
        ),
        migrations.CreateModel(
            name='PartMaintenance',
            fields=[
                ('PartMaintenanceID', models.AutoField(primary_key=True, serialize=False)),
                ('PlaneSN', models.CharField(max_length=10)),
                ('MDS', models.CharField(max_length=10)),
                ('EQP_ID', models.CharField(max_length=5)),
                ('PartSN', models.CharField(max_length=10)),
                ('PartNum', models.CharField(max_length=10)),
                ('Narrative', models.TextField(blank=True, default='')),
                ('WUC_LCN', models.CharField(max_length=14)),
                ('CatNum', models.SmallIntegerField(default=0)),
                ('CrntTime', models.FloatField(default=0.0)),
                ('TimeRemain', models.FloatField(default=0.0)),
                ('DueTime', models.FloatField(default=0.0)),
                ('DueDate', models.DateField()),
                ('Freq', models.SmallIntegerField(default=0)),
                ('Type', models.CharField(max_length=1)),
                ('JST', models.IntegerField(default=0)),
                ('TFrame', models.SmallIntegerField(default=0)),
                ('E_F', models.CharField(max_length=10)),
                ('title', models.TextField(blank=True)),
                ('Scheduled', models.BooleanField(default=False)),
            ],
            options={
                'unique_together': {('PlaneSN', 'MDS', 'title')},
            },
        ),
    ]
