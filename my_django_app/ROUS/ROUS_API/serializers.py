from rest_framework import serializers
from ROUS_API.models import Maintenance_Data, Plane_Data, Calender, User

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance_Data
        # fields = ['aircraft_SN', 'catNum', 'currentTime', 'timeRemain', 'dueTime', 'freq', 'maintenanceType', 'specification']
        fields = "__all__"
        # def create(self, valid_data):
        #     return model.objects.create(**valid_data)
        # def update(self, instance, valid_data):
        #     instance.maintenance_SN = valid_data.get('aircraft_SN')
        #     instance.catNum = valid_data.get('catNum')
        #     instance.currentTime = valid_data.get('currentTime')
        #     instance.timeRemain = valid_data.get('timeRemain')
        #     instance.dueTime = valid_data.get('dueTime')
        #     instance.freq = valid_data.get('freq')
        #     instance.maintenanceType = valid_data.get('maintenanceType')
        #     instance.specification = valid_data.get('specification')
        #     instance.save()
        #     return instance

class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane_Data
        # fields = ['EQP_ID', 'WUC_LCN', 'aircraft_SN', 'maintenance', 'basename', 'aircraftname', 'tailnumber']
        fields = "__all__"
    # def create(self, valid_data):
    #         return model.objects.create(**valid_data)
    # def update(self, instance, valid_data):
    #     instance.EQP_ID = valid_data.get('EQP_ID')
    #     instance.WUC_LCN = valid_data.get('WUC_LCN')
    #     instance.aircraft_SN = valid_data.get('aircraft_SN')
    #     instance.basename = valid_data.get('basename')
    #     instance.aircraftname = valid_data.get('aircraftname')
    #     instance.tailnumber = valid_data.get('tailnumber')
    #     instance.save()
    #     return instance

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        # fields = ['Date', 'tailnumber', 'Reason']
        fields = "__all__"
    # def create(self, valid_data):
    #         return model.objects.create(**valid_data)
    # def update(self, instance, valid_data):
    #     instance.Date = valid_data.get('Date')
    #     instance.tailnumber = valid_data.get('tailnumber')
    #     instance.Reason = valid_data.get('Reason')
    #     instance.save()
    #     return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['firstname', 'lastname', 'username', 'password']
        fields = "__all__"
    # def create(self, valid_data):
    #     return model.objects.create(**valid_data)
    # def update(self, instance, valid_data):
    #     instance.firstname = valid_data.get('firstname')
    #     instance.lastname = valid_data.get('lastname')
    #     instance.username = valid_data.get('username')
    #     instance.password = valid_data.get('password')
    #     instance.save()
    #     return instance