from rest_framework import viewsets
from django.shortcuts import render

from ROUS_API.serializers import MaintenanceSerializer, PlaneSerializer, CalenderSerializer, UserSerializer
from ROUS_API.models import Maintenance_Data, Plane_Data, Calender, User

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return render(request, 'home.html')

# @api_view(["GET", "POST"])
# def MaintenanceView(request):
#     if request.method == "GET":
#         queryset = Maintenance_Data.objects.all()
#         serializerClass = MaintenanceSerializer(queryset, many=True)
#         return JsonResponse(serializerClass.data, status= status.HTTP_200_OK)

#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializerClass = MaintenanceSerializer(data=data)
#         if serializerClass.is_valid():
#             serializerClass.save()
#             return Response(serializerClass.data, status=201)
#         return JsonResponse(serializer.errors, status=300)

# list of maintenances
class MaintenanceView(APIView):
    def get(self, request):
        obj = Maintenance_Data.objects.all()
        serializer = MaintenanceSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# individual maintenances
class MaintenanceInfo(APIView):
    def get(self, request,id):
        try:
            obj = Maintenance_Data.objects.get(id=id)
        except Maintenance_Data.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MaintenanceSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            obj = Maintenance_Data.objects.get(id=id)
        except Maintenance_Data.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MaintenanceSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = Maintenance_Data.objects.get(id=id)
        except Maintenance_Data.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MaintenanceSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = Maintenance_Data.objects.get(id=id)
        except Maintenance_Data.DoesNotExist:
            msg = {"msg": "it aint showin up bud'"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"it's deleted"}, status=status.HTTP_204_NO_CONTENT)

# list of planes
class PlaneView(APIView):
    def get(self, request):
        obj = Plane_Data.objects.all()
        serializer = PlaneSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PlaneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# individual planes
class PlaneInfo(APIView):
    def get(self, request,id):
        try:
            obj = Plane_Data.objects.get(id=id)
        except Plane_Data.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PlaneSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            obj = Plane_Data.objects.get(id=id)
        except Plane_Data.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PlaneSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = Plane_Data.objects.get(id=id)
        except Plane_Data.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PlaneSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = Plane_Data.objects.get(id=id)
        except Plane_Data.DoesNotExist:
            msg = {"msg": "it aint showin up bud'"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"it's deleted"}, status=status.HTTP_204_NO_CONTENT)

# list of calenders
class CalenderView(APIView):
    def get(self, request):
        obj = Calender.objects.all()
        serializer = CalenderSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CalenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# individual calenders
class CalenderInfo(APIView):
    def get(self, request,id):
        try:
            obj = Calender.objects.get(id=id)
        except Calender.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CalenderSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            obj = Calender.objects.get(id=id)
        except Calender.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CalenderSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = Calender.objects.get(id=id)
        except Calender.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CalenderSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = Calender.objects.get(id=id)
        except Calender.DoesNotExist:
            msg = {"msg": "it aint showin up bud'"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"it's deleted"}, status=status.HTTP_204_NO_CONTENT)

# list of users
class UserView(APIView):
    def get(self, request):
        obj = User.objects.all()
        serializer = UserSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# individual users
class UserInfo(APIView):
    def get(self, request,id):
        try:
            obj = User.objects.get(id=id)
        except User_Data.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            obj = User.objects.get(id=id)
        except User.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = User.objects.get(id=id)
        except User_Data.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = User.objects.get(id=id)
        except User.DoesNotExist:
            msg = {"msg": "it aint showin up bud'"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"it's deleted"}, status=status.HTTP_204_NO_CONTENT)