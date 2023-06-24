from django.db import models
from datetime import datetime

# thinking of adding a plane Maintenance and part maintenance to Calendar and then connecting aircraft (calendar) to plane data. then
# Create your models here.
class PlaneMaintenance(models.Model):
    class Meta:
        unique_together = (('PlaneSN', 'MDS', 'JST'),)
    PlaneSN = models.CharField(max_length=10, primary_key=True)
    MDS = models.CharField(max_length=10)
    Narrative = models.TextField(default="", blank=False)
    CrntTime = models.FloatField(null=True, blank=True, default=0.0)
    TimeRemain = models.FloatField(null=True, blank=True, default=0.0)
    DueTime = models.FloatField(null=True, blank=True, default=0.0)
    DueDate = models.DateField(null=True)
    Freq = models.SmallIntegerField(default=0)
    Type = models.CharField(max_length=1)
    JST = models.IntegerField(default=0)
    TFrame = models.SmallIntegerField(default=0)
    E_F = models.CharField(max_length=1)
    # objects = models.Manager()

class PartMaintenance(models.Model):
    class Meta:
        unique_together = (('PlaneSN', 'MDS', 'EQP_ID', 'PartSN', 'PartNum'),)
    PlaneSN = models.CharField(max_length=10)
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
    DueDate = models.DateField()
    Freq = models.SmallIntegerField(default=0)
    Type = models.CharField(max_length=1)
    JST = models.IntegerField(default=0)
    TFrame = models.SmallIntegerField(default=0)
    E_F = models.CharField(max_length=1)

class PlaneData(models.Model):
    class Meta:
        unique_together = (('PlaneSN', 'MDS'),)
    PlaneSN = models.CharField(max_length=10, primary_key=True)
    GeoLoc = models.CharField(max_length=10)
    MDS = models.CharField(max_length=10)
    WUC_LCN = models.CharField(max_length=14)
    EQP_ID = models.CharField(max_length=5)
    TailNumber = models.CharField(max_length=10)
    plane_maintenance = models.OneToOneField(PlaneMaintenance, on_delete=models.CASCADE, related_name='PlaneMaintenance', null=True)
    part_maintenance = models.OneToOneField(PartMaintenance, on_delete=models.CASCADE, related_name='PartMaintenance', null=True)
    # def __str__(self):
    #     return f'{self.PlaneSN}..{self.GeoLoc}'

class Calendar(models.Model):
    start = models.DateField()
    end = models.DateField()
    JulianDate = models.IntegerField(default=0)
    Aircraft = models.CharField(max_length=20, primary_key=True)
    title = models.TextField(blank=True)
    EHours = models.FloatField(null=True, blank=True, default=0.0)
    FHours = models.FloatField(null=True, blank=True, default=0.0)
    GeoLoc = models.CharField(max_length=10)
    aircraft = models.OneToOneField(PlaneData, on_delete=models.CASCADE, related_name='aircraft', null=True)

