from rest_framework import serializers
from .models import *

class PlaneDataSerializer(serializers.ModelSerializer):
    plane_maintenance = serializers.SerializerMethodField()
    part_maintenance = serializers.SerializerMethodField()
    def get_plane_maintenance(self, obj):
        planesn = obj.PlaneSN
        mds = obj.MDS
        plane_maintenance_instance = PlaneMaintenance.objects.filter(MDS=mds, PlaneSN=planesn).first()
        if plane_maintenance_instance is not None:
            return PlaneMaintenanceSerializer(plane_maintenance_instance).data
        else:
            return {}

    def get_part_maintenance(self, obj):
        planesn = obj.PlaneSN
        mds = obj.MDS
        part_maintenance_instance = PartMaintenance.objects.filter(MDS=mds, PlaneSN=planesn).first()
        if part_maintenance_instance is not None:
            return PartMaintenanceSerializer(part_maintenance_instance).data
        else:
            return {}
    class Meta:
        model = PlaneData
        fields = '__all__'

class CalendarSerializer(serializers.ModelSerializer):
    aircraft = serializers.SerializerMethodField()

    def get_aircraft(self, obj):
        aircraft_identifier = obj.Aircraft  # Assuming 'aircraft' field contains the concatenated MDS and TailNumber
        mds = aircraft_identifier[:4]  # Extract the first three characters as MDS
        tail_number = aircraft_identifier[4:]  # Extract the remaining characters as TailNumber

        aircraft_instance = PlaneData.objects.filter(MDS=mds, TailNumber=tail_number).first()
        if aircraft_instance is not None:
            return PlaneDataSerializer(aircraft_instance).data
        else:
            return {}

    class Meta:
        model = Calendar
        fields = '__all__'


class PlaneMaintenanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlaneMaintenance
        fields = '__all__'

class PartMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartMaintenance
        fields = '__all__'