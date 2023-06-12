from django.db import models
from datetime import datetime


# Create your models here.
class PlaneData(models.Model):
    class Meta:
        unique_together = (('PlaneSN', 'MDS'),)
    PlaneSN = models.CharField(max_length=10, primary_key=True)
    GeoLoc = models.CharField(max_length=10)
    MDS = models.CharField(max_length=10)
    WUC_LCN = models.CharField(max_length=14)
    EQP_ID = models.CharField(max_length=5)
    TailNumber = models.CharField(max_length=10)
    # objects = models.Manager()

    def __str__(self):
        return f'{self.PlaneSN}..{self.GeoLoc}'

class Calendar(models.Model):
    StartDate = models.DateField()
    EndDate = models.DateField()
    Aircraft = models.CharField(max_length=20, primary_key=True)
    Reason = models.TextField(blank=True)
    EHours = models.FloatField(null=True, blank=True, default=0.0)
    FHours = models.FloatField(null=True, blank=True, default=0.0)
    GeoLoc = models.CharField(max_length=10)
    # objects = models.Manager()


class PlaneMaintenance(models.Model):
    class Meta:
        unique_together = (('PlaneSN', 'MDS'),)
    PlaneSN = models.CharField(max_length=10, primary_key=True)
    MDS = models.CharField(max_length=10)
    Narrative = models.TextField(blank=False)
    CrntTime = models.FloatField(null=True, blank=True, default=0.0)
    TimeRemain = models.FloatField(null=True, blank=True, default=0.0)
    DueTime = models.FloatField(null=True, blank=True, default=0.0)
    DueDate = models.DateField(null=True)
    Freq = models.SmallIntegerField()
    Type = models.CharField(max_length=1)
    JST = models.IntegerField()
    TFrame = models.SmallIntegerField()
    E_F = models.CharField(max_length=1)
    # objects = models.Manager()


class PartMaintenance(models.Model):
    class Meta:
        unique_together = (('PlaneSN', 'MDS', 'EQP_ID', 'PartSN', 'PartNum'),)
    PlaneSN = models.CharField(max_length=10)
    MDS = models.CharField(max_length=10)
    EQP_ID = models.CharField(max_length=5, primary_key=True)
    PartSN = models.CharField(max_length=10)
    PartNum = models.CharField(max_length=10)
    Narrative = models.TextField(blank=True)
    WUC_LCN = models.CharField(max_length=14)
    CatNum = models.SmallIntegerField()
    CrntTime = models.FloatField()
    TimeRemain = models.FloatField()
    DueTime = models.FloatField()
    DueDate = models.DateField()
    Freq = models.SmallIntegerField()
    Type = models.CharField(max_length=1)
    JST = models.IntegerField()
    TFrame = models.SmallIntegerField()
    E_F = models.CharField(max_length=1)
    # objects = models.Manager()
