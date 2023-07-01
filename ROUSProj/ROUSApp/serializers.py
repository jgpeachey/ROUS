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
    class Meta:
        model = PlaneData
        fields = '__all__'

class CalendarSerializer(serializers.ModelSerializer):
    maintenance = serializers.SerializerMethodField()

    def get_maintenance(self, obj):
        # planesn = obj.PlaneSN
        # mds = obj.MDS
        title = obj.title
        plane_maintenance_instance = PlaneMaintenance.objects.filter(title=title).first()
        part_maintenance_instance = PartMaintenance.objects.filter(title=title).first()
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

