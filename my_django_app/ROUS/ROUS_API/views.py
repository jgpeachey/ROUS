from rest_framework import viewsets

from ROUS_API.serializers import MaintenanceSerializer, PlaneSerializer, CalenderSerializer, UserSerializer
from ROUS_API.models import Maintenance_Data, Plane_Data, Calender, User

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def MaintenanceView(request):
    if request.method == 'GET':
        queryset = Maintenance_Data.objects.all()
        serializerClass = MaintenanceSerializer(queryset, many=True)
        return JsonResponse(serializerClass.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializerClass = MaintenanceSerializer(data=data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data, status=201)
        return JsonResponse(serializer.errors, statud=300)

@api_view(['GET', 'POST'])
def PlaneView(request):
    if request.method == 'GET':
        queryset = Plane_Data.objects.all()
        serializerClass = PlaneSerializer(queryset, many=True)
        return JsonResponse(serializerClass.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializerClass = PlaneSerializer(data=data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def CalenderView(request):
    if request.method == 'GET':
        queryset = Calender.objects.all()
        serializerClass = CalenderSerializer(queryset, many=True)
        return JsonResponse(serializerClass.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializerClass = CalenderSerializer(data=data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def UserView(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializerClass = UserSerializer(queryset, many=True)
        return JsonResponse(serializerClass.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializerClass = UserSerializer(data=data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data, status=status.HTTP_201_CREATED)

