from django.db import models

class catNum(models.Model):
    catNum = models.CharField(max_length = 10)

class engine_current_time(models.Model):
    engine_current_time = models.CharField(max_length = 10)

class Aircraft(models.Model):
    tailnumber = models.CharField(max_length = 10)
    aircraft_type = models.CharField(max_length = 10)
    # name = models.CharField(max_length = 10)
    EQP_ID = models.CharField(max_length = 10)
    EQP_SN = models.CharField(max_length = 10)
    catNum = models.ForeignKey(catNum, on_delete= models.DO_NOTHING)
    aircraft_SN = models.CharField(max_length = 10)
    engine_current_time = models.ForeignKey(engine_current_time, on_delete= models.DO_NOTHING)
    aircraft_current_time = models.CharField(max_length = 100)
    position = models.CharField(max_length = 10)
    status = models.CharField(max_length = 10)

class Base(models.Model):
    basename = models.CharField(max_length = 100)
    aircrafts = models.ForeignKey(Aircraft, on_delete=models.DO_NOTHING)

class User(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    base = models.ForeignKey(Base, on_delete= models.DO_NOTHING)
