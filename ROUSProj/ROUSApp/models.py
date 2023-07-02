from django.db import models
# from datetime import datetime
# import uuid

# from .views import MaintenanceAircraftView


# thinking of adding a plane Maintenance and part maintenance to Calendar and then connecting aircraft (calendar) to plane data. then
# Create your models here.

class Location(models.Model):
    GeoLoc = models.CharField(primary_key=True, max_length=10)

class PlaneMaintenance(models.Model):
    # class Meta:
    #     unique_together = (('PlaneSN', 'MDS', 'JST'),)
    PlaneMaintenanceID = models.AutoField(primary_key=True)
    PlaneSN = models.CharField(max_length=10)
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
    title = models.TextField(blank=True)

    class Meta:
        unique_together = (('PlaneSN', 'MDS', 'title'),)
    # objects = models.Manager()

class PartMaintenance(models.Model):
    # class Meta:
    #     unique_together = (('PlaneSN', 'MDS', 'EQP_ID', 'PartSN', 'PartNum'),)
    PartMaintenanceID = models.AutoField(primary_key=True)
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
    title = models.TextField(blank=True)
    class Meta:
        unique_together = (('PlaneSN', 'MDS', 'title'),)

# multiple maintenances in plane_maintenance and part_maintenance
class PlaneData(models.Model):
    class Meta:
        unique_together = (('PlaneSN', 'MDS'),)

    PlaneSN = models.CharField(max_length=10, primary_key=True)
    GeoLoc = models.CharField(max_length=10)
    MDS = models.CharField(max_length=10)
    WUC_LCN = models.CharField(max_length=14)
    EQP_ID = models.CharField(max_length=5)
    TailNumber = models.CharField(max_length=10)

    # @property
    # def maintenances(self):
    #     view = MaintenanceAircraftView()
    #     return view.get_combined_maintenances(self.PlaneSN, self.MDS)

# a single maintenance that matches the title
class Calendar(models.Model):
    start = models.DateField()
    end = models.DateField()
    CalendarID = models.AutoField(primary_key=True)
    JulianDate = models.IntegerField(default=0)
    Aircraft = models.CharField(max_length=20)
    title = models.TextField(blank=True)
    EHours = models.FloatField(null=True, blank=True, default=0.0)
    FHours = models.FloatField(null=True, blank=True, default=0.0)
    GeoLoc = models.CharField(max_length=10)
    PlaneMaintenanceID = models.IntegerField(default=0)
    PartMaintenanceID = models.IntegerField(default=0)


    # aircraft = models.OneToOneField(PlaneData, on_delete=models.CASCADE, related_name='aircraft', null=True)
