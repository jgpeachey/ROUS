from rest_framework import serializers
from ROUS_API.models import Maintenance_Data, Plane_Data, Calender, User

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance_Data
        fields = ['maintenance_SN', 'catNum', 'currentTime', 'timeRemain', 'dueTime', 'freq', 'maintenanceType', 'specification']

class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane_Data
        fields = ['EQP_ID', 'WUC_LCN', 'aircraft_SN', 'maintenance', 'basename', 'aircraftname', 'tailnumber']

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = ['Date', 'aircraft', 'Reason']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'password']