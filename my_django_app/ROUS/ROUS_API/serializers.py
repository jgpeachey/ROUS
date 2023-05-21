from rest_framework import serializers
from ROUS_API.models import User, Base, Aircraft, catNum, engine_current_time

class CatNumSerializer(serializers.ModelSerializer):
    class Meta:
        model: catNum
        fields = ['catnum']

class EngineCurrentTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model: engine_current_time
        fields =['engine_current_time']

class AircraftSerializer(serializers.ModelSerializer):
    catNumList = CatNumSerializer(many=True, read_only=True)
    engine_current_time_list  = EngineCurrentTimeSerializer(many=True, read_only=True)
    class Meta:
        model = Aircraft
        fields = ['tailnumber', 'aircraft_type', 'EQP_ID', 'EQP_SN', 'catNumList', 'aircraft_SN', 'engine_current_time_list', 'aircraft_current_time', 'position', 'status']

class BaseSerializer(serializers.ModelSerializer):
    aircrafts = AircraftSerializer(many=True, read_only=True)
    class Meta:
        model =  Base
        fields = ['basename', 'aircrafts']

class UserSerializer(serializers.ModelSerializer):
    bases = BaseSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'password', 'bases']




