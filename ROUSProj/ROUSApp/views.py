from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status, generics
from rest_framework.views import APIView
# gotta pip install pandas  and openpyxl first
import pandas as pd
from datetime import datetime
from pandas._libs.tslibs.nattype import NaTType
import numpy as np
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
    def delete(self, request, pk1):
        try:
            obj = Calendar.objects.get(CalendarID=pk1)
        except Calendar.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg": "it's deleted"}, status=status.HTTP_204_NO_CONTENT)

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

class CalendarPlaneMaintenanceView(APIView):
    def get(self, request, pk1):
        try:
            obj = PlaneMaintenance.objects.get(PlaneMaintenanceID=pk1)
        except PlaneMaintenance.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = PlaneMaintenanceSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk1):
        try:
            obj = PlaneMaintenance.objects.get(PlaneMaintenanceID=pk1)
        except PlaneMaintenance.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = PlaneMaintenanceSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk1):
        try:
            obj = PlaneMaintenance.objects.get(PlaneMaintenanceID=pk1)
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

class CalendarPartMaintenanceView(APIView):
    def get(self, request, pk1):
        try:
            obj = PartMaintenance.objects.get(PartMaintenanceID=pk1)
        except PartMaintenance.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = PartMaintenanceSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk1):
        try:
            obj = PartMaintenance.objects.get(PartMaintenanceID=pk1)
        except PartMaintenance.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        print(request.data)

        serializer = PartMaintenanceSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class IndividualResourceView(APIView):
    def get(self, request, pk1, pk2):
        try:
            obj = Resource.objects.get(TailNumber=pk1, GeoLoc=pk2)
        except Resource.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = ResourceSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def patch(self, request, pk1, pk2):
        try:
            obj = Resource.objects.get(TailNumber=pk1, GeoLoc=pk2)
        except Resource.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = ResourceSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PostResourceView(APIView):
    def get(self, request):
        obj = Resource.objects.all()
        serializer = ResourceSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class IndividualLocationResourceView(generics.ListAPIView):
    serializer_class = ResourceSerializer
    def get_queryset(self):
        geoloc = self.kwargs['GeoLoc']
        return Resource.objects.filter(GeoLoc=geoloc)

# a part of parser when the time comes
# def parse_datetime(value):
#     if pd.isnull(value) or value == 'NaT':
#         return None
#     try:
#         parsed_value = datetime.strptime(str(value), '%Y-%m-%d')
#         return parsed_value
#     except (ValueError, TypeError):
#         print(f"Failed to parse datetime value: {value}")
#         return None
#
# def parse_julian_date(value):
#     if isinstance(value, NaTType):
#         return 0  # Set a default value or handle it based on your requirements
#     try:
#         return int(value)
#     except (ValueError, TypeError):
#         return 0

# supposed to process parsed excel sheet data for calendar
class ExcelImportCalendarDataView(APIView):
    def post(self, request, file):
    #     file = request.FILES.get('excel_file')
        if file is None:
            return Response({'error': 'No file uploaded.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            df = pd.read_excel(file)
            df = df.replace({np.nan: None})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        for _, row in df.iterrows():
            calendar_data = Calendar(
                start= row['start'],
                end= row['end'],
                JulianDate= row['JulianDate'],
                MDS= row['MDS'],
                GeoLoc= row['GeoLoc'],
                TailNumber= row['TailNumber'],
                title= row['title'],
                EHours= row['EHours'],
                FHours= row['FHours'],
                # Populate other fields accordingly
            )
            try:
                calendar_data.save()
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': 'Data imported successfully.'})

# supposed to process parsed excel sheet data for part maintenance, plane maintenance, plane data
class ExcelImportView(APIView):
    def post(self, request, file):
    #     file = request.FILES.get('excel_file')
        if file is None:
            return Response({'error': 'No file uploaded.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            df = pd.read_excel(file)
            df = df.replace({np.nan: None})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        for _, row in df.iterrows():
            plane_sn = row['PlaneSN']
            print("PlaneSN: ", plane_sn)
            plane_maintenance = PlaneMaintenance(
                PlaneSN=plane_sn,
                Narrative=row['Narrative'],
                CrntTime=row['CrntTime'],
                TimeRemain=row['TimeRemain'],
                DueTime=row['DueTime'],
                # DueDate=row['DueDate'],  # Uncomment if DueDate is available in the DataFrame
                Freq=int(row['Freq']) if pd.notnull(row['Freq']) else None,
                Type=row['Type'],
                JST=row['JST'],
                TFrame=int(row['TFrame']) if pd.notnull(row['TFrame']) else None,
                E_F=row['E_F'],
                title=row['title'],
                # Set other fields accordingly
            )

            try:
                plane_maintenance.save()
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            part_maintenance = PartMaintenance(
                PlaneSN= plane_sn,
                MDS= row['MDS'],
                EQP_ID= row['EQP_ID'],
                PartSN= row['PartSN'],
                PartNum= row['PartNum'],
                Narrative= row['Narrative'],
                WUC_LCN= row['WUC_LCN'],
                CatNum= row['CatNum'],
                CrntTime= row['CrntTime'],
                TimeRemain= row['TimeRemain'],
                DueTime= row['DueTime'],
                DueDate= row['DueDate'],
                Freq= int(row['Freq']) if pd.notnull(row['Freq']) else None,
                Type= row['Type'],
                JST= row['JST'],
                TFrame= int(row['TFrame']) if pd.notnull(row['TFrame']) else None,
                E_F= row['E_F'],
                title= row['title'],
                # Populate other fields accordingly
            )
            try:
                part_maintenance.save()
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            plane_data = PlaneData(
                PlaneSN= plane_sn,
                MDS= row['MDS'],
                EQP_ID= row['EQP_ID'],
                WUC_LCN= row['WUC_LCN'],
                GeoLoc= row['GeoLoc'],
                TailNumber= row['TailNumber'],
                # Populate other fields accordingly
            )
            try:
                plane_data.save()
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'Data imported successfully.'})
