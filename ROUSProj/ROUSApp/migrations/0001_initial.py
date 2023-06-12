# Generated by Django 4.2.2 on 2023-06-09 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('Aircraft', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('GeoLoc', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PlaneMaintenance',
            fields=[
                ('PlaneSN', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('MDS', models.CharField(max_length=10)),
                ('Type', models.CharField(max_length=1)),
                ('E_F', models.CharField(max_length=1)),
            ],
            options={
                'unique_together': {('PlaneSN', 'MDS')},
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
            ],
            options={
                'unique_together': {('PlaneSN', 'MDS')},
            },
        ),
        migrations.CreateModel(
            name='PartMaintenance',
            fields=[
                ('EQP_ID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('PartSN', models.CharField(max_length=10)),
                ('PartNum', models.CharField(max_length=10)),
                ('WUC_LCN', models.CharField(max_length=14)),
                ('Type', models.CharField(max_length=1)),
                ('E_F', models.CharField(max_length=1)),
                ('MDS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MDSs', to='ROUSApp.planedata')),
                ('PlaneSN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PartMaintenance', to='ROUSApp.planedata')),
            ],
            options={
                'unique_together': {('PlaneSN', 'MDS', 'EQP_ID', 'PartSN', 'PartNum')},
            },
        ),
    ]
