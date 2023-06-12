from rest_framework import serializers
from .models import *

class PlaneDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaneData
        fields = '__all__'

class CalendarSerializer(serializers.ModelSerializer):
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