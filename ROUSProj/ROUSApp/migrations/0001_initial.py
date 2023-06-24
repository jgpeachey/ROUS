# Generated by Django 4.2.2 on 2023-06-24 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('E_F', models.CharField(max_length=1)),
            ],
            options={
                'unique_together': {('PlaneSN', 'MDS', 'EQP_ID', 'PartSN', 'PartNum')},
            },
        ),
        migrations.CreateModel(
            name='PlaneMaintenance',
            fields=[
                ('PlaneSN', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('MDS', models.CharField(max_length=10)),
                ('Narrative', models.TextField(default='')),
                ('CrntTime', models.FloatField(blank=True, default=0.0, null=True)),
                ('TimeRemain', models.FloatField(blank=True, default=0.0, null=True)),
                ('DueTime', models.FloatField(blank=True, default=0.0, null=True)),
                ('DueDate', models.DateField(null=True)),
                ('Freq', models.SmallIntegerField(default=0)),
                ('Type', models.CharField(max_length=1)),
                ('JST', models.IntegerField(default=0)),
                ('TFrame', models.SmallIntegerField(default=0)),
                ('E_F', models.CharField(max_length=1)),
            ],
            options={
                'unique_together': {('PlaneSN', 'MDS', 'JST')},
            },
        ),
        migrations.CreateModel(
            name='PlaneData',
            fields=[
                ('PlaneSN', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('GeoLoc', models.CharField(max_length=10)),
                ('MDS', models.CharField(max_length=10)),
                ('WUC_LCN', models.CharField(max_length=14)),
                ('EQP_ID', models.CharField(max_length=5)),
                ('TailNumber', models.CharField(max_length=10)),
                ('part_maintenance', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PartMaintenance', to='ROUSApp.partmaintenance')),
                ('plane_maintenance', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PlaneMaintenance', to='ROUSApp.planemaintenance')),
            ],
            options={
                'unique_together': {('PlaneSN', 'MDS')},
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('JulianDate', models.IntegerField(default=0)),
                ('Aircraft', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True)),
                ('EHours', models.FloatField(blank=True, default=0.0, null=True)),
                ('FHours', models.FloatField(blank=True, default=0.0, null=True)),
                ('GeoLoc', models.CharField(max_length=10)),
                ('aircraft', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aircraft', to='ROUSApp.planedata')),
            ],
        ),
    ]
