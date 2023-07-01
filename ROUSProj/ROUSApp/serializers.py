from rest_framework import serializers
from .models import *

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class PlaneMaintenanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlaneMaintenance
        fields = '__all__'

    # def validate(self, attrs):
    #     return attrs


class PartMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartMaintenance
        fields = '__all__'

    # def validate(self, attrs):
    #     return attrs


class PlaneDataSerializer(serializers.ModelSerializer):
    plane_maintenances = serializers.SerializerMethodField()
    part_maintenances = serializers.SerializerMethodField()

    def get_plane_maintenances(self, obj):
        PlaneSN = obj.PlaneSN
        MDS = obj.MDS
        plane_maintenance_instances = PlaneMaintenance.objects.filter(PlaneSN=PlaneSN, MDS=MDS)
        plane_maintenance_data = PlaneMaintenanceSerializer(plane_maintenance_instances, many=True).data

        return plane_maintenance_data
    def get_part_maintenances(self, obj):
        PlaneSN = obj.PlaneSN
        MDS = obj.MDS
        part_maintenance_instances = PartMaintenance.objects.filter(PlaneSN=PlaneSN, MDS=MDS)
        part_maintenance_data = PartMaintenanceSerializer(part_maintenance_instances, many=True).data

        return  part_maintenance_data

    class Meta:
        model = PlaneData
        fields = '__all__'


class CalendarSerializer(serializers.ModelSerializer):
    maintenance = serializers.SerializerMethodField()

    def get_maintenance(self, obj):
        # planesn = obj.PlaneSN
        # mds = obj.MDS
        PlaneMaintenanceID = obj.PlaneMaintenanceID
        PartMaintenanceID = obj.PartMaintenanceID
        plane_maintenance_instance = PlaneMaintenance.objects.filter(PlaneMaintenanceID=PlaneMaintenanceID).first()
        part_maintenance_instance = PartMaintenance.objects.filter(PartMaintenanceID=PartMaintenanceID).first()
        if plane_maintenance_instance is not None:
            return PlaneMaintenanceSerializer(plane_maintenance_instance).data
        else:
            if part_maintenance_instance is not None:
                return PartMaintenanceSerializer(part_maintenance_instance).data
            else:
                return {}

    class Meta:
        model = Calendar
        fields = '__all__'

