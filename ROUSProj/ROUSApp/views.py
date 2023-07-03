from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status, generics
from rest_framework.views import APIView

# views.py

def home(request):
    return render(request, 'home.html')

def fileupload(request):
    return render(request, 'fileupload.html')

def calendar(request):
    return render(request, 'calendar.html')

def location(request):
    return render(request, 'location.html')

class PlaneListView(APIView):
    def get(self, request):
        obj = PlaneData.objects.all()
        serializer = PlaneDataSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlaneDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IndividualPlaneData(APIView):
    def get(self, request, pk1, pk2):
        try:
            obj = PlaneData.objects.get(PlaneSN=pk1, MDS=pk2)
        except PlaneData.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = PlaneDataSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk1, pk2):
        try:
            obj = PlaneData.objects.get(PlaneSN=pk1, MDS=pk2)
        except PlaneData.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = PlaneDataSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk1, pk2):
        try:
            obj = PlaneData.objects.get(PlaneSN=pk1, MDS=pk2)
        except PlaneData.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg": "it's deleted"}, status=status.HTTP_204_NO_CONTENT)

class CalendarListView(APIView):
    def get(self, request):
        obj = Calendar.objects.all()
        serializer = CalendarSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CalendarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IndividualAircraftCalendar(APIView):
    def get(self, request, pk1, pk2):
        try:
            obj = Calendar.objects.get(MDS=pk1, TailNumber=pk2)
        except Calendar.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = CalendarSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk1, pk2):
        try:
            obj = Calendar.objects.get(MDS=pk1, TailNumber=pk2)
        except Calendar.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg": "it's deleted"}, status=status.HTTP_204_NO_CONTENT)

class IndividualDateCalendarEdit(APIView):
    def get(self, request, pk1):
        try:
            obj = Calendar.objects.get(CalendarID=pk1)
        except Calendar.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = CalendarSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def patch(self, request, pk1):
        try:
            obj = Calendar.objects.get(CalendarID=pk1)
        except PlaneMaintenance.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = CalendarSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaneMaintenanceListView(APIView):
    def get(self, request):
        obj = PlaneMaintenance.objects.all()
        serializer = PlaneMaintenanceSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlaneMaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IndividualPlaneMaintenanceView(APIView):
    def get(self, request, pk1, pk2, pk3):
        try:
            obj = PlaneMaintenance.objects.get(PlaneSN=pk1, MDS=pk2, JST=pk3)
        except PlaneMaintenance.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = PlaneMaintenanceSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk1, pk2, pk3):
        try:
            obj = PlaneMaintenance.objects.get(PlaneSN=pk1, MDS=pk2, JST=pk3)
        except PlaneMaintenance.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = PlaneMaintenanceSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk1, pk2, pk3):
        try:
            obj = PlaneMaintenance.objects.get(PlaneSN=pk1, MDS=pk2, JST=pk3)
        except PlaneMaintenance.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg": "it's deleted"}, status=status.HTTP_204_NO_CONTENT)

# class PlaneMaintenanceAircraftView(APIView):
#     def delete(self, request, pk1, pk2):
#         try:
#             obj = PlaneMaintenance.objects.get(PlaneSN=pk1, MDS=pk2)
#         except PlaneMaintenance.DoesNotExist:
#             msg = {"msg": "not found"}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
#         obj.delete()
#         return Response({"msg": "it's deleted"}, status=status.HTTP_204_NO_CONTENT)
#
#     def get(self, request, pk1, pk2):
#         objs = PlaneMaintenance.objects.filter(PlaneSN=pk1, MDS=pk2)
#         if not objs:
#             msg = {"msg": "not found"}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
#         objs = objs.order_by('TimeRemain')
#         serializer = PlaneMaintenanceSerializer(objs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class PartMaintenanceListView(APIView):
    def get(self, request):
        obj = PartMaintenance.objects.all()
        serializer = PartMaintenanceSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = PartMaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IndividualPartMaintenanceView(APIView):
    def get(self, request, pk1, pk2, pk3, pk4, pk5):
        try:
            obj = PartMaintenance.objects.get(PlaneSN=pk1, MDS=pk2, EQP_ID=pk3, PartSN=pk4, PartNum=pk5)
        except PartMaintenance.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = PartMaintenanceSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk1, pk2, pk3, pk4, pk5):
        try:
            obj = PartMaintenance.objects.get(PlaneSN=pk1, MDS=pk2, EQP_ID=pk3, PartSN=pk4, PartNum=pk5)
        except PartMaintenance.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = PartMaintenanceSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk1, pk2, pk3, pk4, pk5):
        try:
            obj = PartMaintenance.objects.get(PlaneSN=pk1, MDS=pk2, EQP_ID=pk3, PartSN=pk4, PartNum=pk5)
        except PartMaintenance.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg": "it's deleted"}, status=status.HTTP_204_NO_CONTENT)

# class PartMaintenanceAircraftView(APIView):
#     def delete(self, request, pk1, pk2):
#         try:
#             obj = PartMaintenance.objects.get(PlaneSN=pk1, MDS=pk2)
#         except PartMaintenance.DoesNotExist:
#             msg = {"msg": "not found"}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
#         obj.delete()
#         return Response({"msg": "it's deleted"}, status=status.HTTP_204_NO_CONTENT)
#
#     def get(self, request, pk1, pk2):
#         objs = PartMaintenance.objects.filter(PlaneSN=pk1, MDS=pk2)
#         if not objs:
#             msg = {"msg": "not found"}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
#         objs = objs.order_by('TimeRemain')
#         serializer = PartMaintenanceSerializer(objs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class LocationList(APIView):
    def get(self, request):
        obj = Location.objects.all()
        serializer = LocationSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'GeoLoc'
    def delete(self, request, pk):
        try:
            obj = Location.objects.get(GeoLoc=pk)
        except Location.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg": "it's deleted"}, status=status.HTTP_204_NO_CONTENT)

class CalendarListByGeoLoc(generics.ListAPIView):
    serializer_class = CalendarSerializer

    def get_queryset(self):
        geoloc = self.kwargs['GeoLoc']
        return Calendar.objects.filter(GeoLoc=geoloc)