from rest_framework import viewsets

from ROUS_API.serializers import UserSerializer, BaseSerializer, AircraftSerializer, CatNumSerializer, EngineCurrentTimeSerializer
from ROUS_API.models import User, Base, Aircraft, catNum, engine_current_time

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def UserView(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializerClass = UserSerializer(queryset, many=True)
        return JsonResponse(serializerClass.data, safe=False)
    if request.method == 'POST':
        serializerClass = UserSerializer(data=request.data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def BaseView(request):
    if request.method == 'GET':
        queryset = Base.objects.all()
        serializerClass = BaseSerializer(queryset, many=True)
        return JsonResponse(serializerClass.data, safe=False)
    if request.method == 'POST':
        serializerClass = BaseSerializer(data=request.data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def AircraftView(request):
    if request.method == 'GET':
        queryset = Aircraft.objects.all()
        serializerClass = AircraftSerializer(queryset, many=True)
        return JsonResponse(serializerClass.data, safe=False)
    if request.method == 'POST':
        serializerClass = AircraftSerializer(data=request.data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def CatNumView(request):
    if request.method == 'GET':
        queryset = catNum.objects.all()
        serializerClass = CatNumSerializer(queryset, many=True)
        return JsonResponse(serializerClass.data, safe=False)
    if request.method == 'POST':
        serializerClass = CatNumSerializer(data=request.data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def EngineCurrentTimeView(request):
    if request.method == 'GET':
        queryset = engine_current_time.objects.all()
        serializerClass = EngineCurrentTimeSerializer(queryset, many=True)
        return JsonResponse(serializerClass.data, safe=False)
    if request.method == 'POST':
        serializerClass = EngineCurrentTimeSerializer(data=request.data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data, status=status.HTTP_201_CREATED)
