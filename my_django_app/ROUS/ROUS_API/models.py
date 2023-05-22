from django.db import models

# class catNum(models.Model):
#     catNum = models.CharField(max_length = 10)

# class engine_current_time(models.Model):
#     engine_current_time = models.CharField(max_length = 10)

class Maintenance_Data(models.Model):
    aircraft_SN = models.CharField(max_length = 10)
    catNum = models.IntegerField()
    currentTime = models.IntegerField()
    timeRemain = models.IntegerField()
    dueTime = models.IntegerField()
    freq = models.IntegerField()
    maintenanceType = models.CharField(max_length = 6)
    specification = models.IntegerField()


class Plane_Data(models.Model):
    EQP_ID = models.CharField(max_length = 10)
    WUC_LCN = models.CharField(max_length = 10)
    aircraft_SN = models.CharField(max_length = 10)
    basename = models.CharField(max_length = 10)
    aircraftname = models.CharField(max_length = 10)
    tailnumber = models.CharField(max_length = 10)

class Calender(models.Model):
    Date = models.DateField()
    tailnumber = models.CharField(max_length = 10)
    Reason = models.CharField(max_length= 200)

class User(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
