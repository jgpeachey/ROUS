# models.py
from django.db import models

class Location(models.Model):
    GeoLoc = models.CharField(primary_key=True, max_length=10)

class Resource(models.Model):
    ResourceID = models.AutoField(primary_key=True)
    TailNumber = models.CharField(max_length=10)
    GeoLoc = models.CharField(max_length=10)

class PlaneMaintenance(models.Model):
    PlaneMaintenanceID = models.AutoField(primary_key=True)
    PlaneSN = models.CharField(max_length=10, blank=True)
    MDS = models.CharField(max_length=10)
    Narrative = models.TextField(default="", blank=False)
    CrntTime = models.FloatField(null=True, blank=True, default=0.0)
    TimeRemain = models.FloatField(null=True, blank=True, default=0.0)
    DueTime = models.FloatField(null=True, blank=True, default=0.0)
    Freq = models.SmallIntegerField(null=True, blank=True, default=0)
    Type = models.CharField(max_length=1)
    JST = models.IntegerField(default=0)
    TFrame = models.SmallIntegerField(null=True, blank=True, default=0)
    E_F = models.CharField(max_length=1, blank=True, null=True)
    title = models.TextField(blank=True)

    class Meta:
        unique_together = (('PlaneSN', 'MDS', 'title'),)

class PartMaintenance(models.Model):
    PartMaintenanceID = models.AutoField(primary_key=True)
    PlaneSN = models.CharField(max_length=10, blank=True)
    MDS = models.CharField(max_length=10)
    EQP_ID = models.CharField(max_length=5)
    PartSN = models.CharField(max_length=10)
    PartNum = models.CharField(max_length=10)
    Narrative = models.TextField(default="", blank=True)
    WUC_LCN = models.CharField(max_length=14)
    CatNum = models.SmallIntegerField(default=0)
    CrntTime = models.FloatField(default=0.0)
    TimeRemain = models.FloatField(default=0.0)
    DueTime = models.FloatField(default=0.0)
    DueDate = models.DateField(blank=True)
    Freq = models.SmallIntegerField(null=True, blank=True, default=0)
    Type = models.CharField(max_length=1)
    JST = models.IntegerField(default=0)
    TFrame = models.SmallIntegerField(null=True, blank=True, default=0)
    E_F = models.CharField(max_length=1, blank=True, null=True)
    title = models.TextField(blank=True)

    class Meta:
        unique_together = (('PlaneSN', 'MDS', 'title'),)

class PlaneData(models.Model):
    PlaneSN = models.CharField(max_length=10, primary_key=True, blank=True)
    GeoLoc = models.CharField(max_length=10)
    MDS = models.CharField(max_length=10)
    WUC_LCN = models.CharField(max_length=14)
    EQP_ID = models.CharField(max_length=5)
    TailNumber = models.CharField(max_length=10)

    class Meta:
        unique_together = (('PlaneSN', 'MDS'),)

class Calendar(models.Model):
    start = models.DateField()
    end = models.DateField()
    CalendarID = models.AutoField(primary_key=True)
    JulianDate = models.IntegerField(default=0)
    MDS = models.CharField(max_length=10)
    TailNumber = models.CharField(max_length=10)
    title = models.TextField(blank=True)
    EHours = models.FloatField(null=True, blank=True, default=0.0)
    FHours = models.FloatField(null=True, blank=True, default=0.0)
    GeoLoc = models.CharField(max_length=10)
    PlaneMaintenanceID = models.IntegerField(default=0)
    PartMaintenanceID = models.IntegerField(default=0)
    ResourceID = models.IntegerField(default=0)

class ExcelFileUpload(models.Model):
    excel_file_upload = models.FileField(upload_to='excel')
