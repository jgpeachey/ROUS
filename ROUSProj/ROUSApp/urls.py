

from django.urls import path
from . import views

from django.urls import path, register_converter
from datetime import date

class DateConverter:
    regex = r'\d{4}-\d{2}-\d{2}'
    def to_python(self, value):
        return date.fromisoformat(value)

    def to_url(self, value):
        return value.isoformat()

register_converter(DateConverter, 'date')

urlpatterns = [
    path('', views.home, name='home'),
    path('location.html', views.location, name='location'),
    path('calendar.html', views.calendar, name='calendar'),
    path('fileupload.html', views.fileupload, name='fileupload'),
    path("plane-data/", views.PlaneListView.as_view(), name='planes'),
    path("plane-data/<str:pk1>/<str:pk2>/", views.IndividualPlaneData.as_view(), name='plane details'),
    path("calendar/", views.CalendarListView.as_view(), name='calendars'),
    path("calendar/<str:pk1>/<date:pk2>/", views.IndividualDateCalendarEdit.as_view(), name='calendar date details'),
    path("calendar/aircraft/<str:pk>/", views.IndividualAircraftCalendar.as_view(), name='calendar-edit-details'),
    path("plane-maintenance/", views.PlaneMaintenanceListView.as_view(), name='plane maintenance'),
    path("plane-maintenance/<str:pk1>/<str:pk2>/<int:pk3>/", views.IndividualPlaneMaintenanceView.as_view(), name='plane main details'),
    path("plane-maintenance/<str:pk1>/<str:pk2>/", views.PlaneMaintenanceAircraftView.as_view(), name='plane main aircraft detail'),
    path("part-maintenance/", views.PartMaintenanceListView.as_view(), name='part maintenance'),
    path("part-maintenance/<str:pk1>/<str:pk2>/<str:pk3>/<str:pk4>/<str:pk5>/", views.IndividualPartMaintenanceView.as_view(), name='part main details'),
    path("part-maintenance/<str:pk>/", views.PartMaintenanceAircraftView.as_view(), name='part main aircraft details'),
    path('loc/', views.LocationList.as_view(), name='location-list'),
    path('loc/<str:pk>/', views.LocationDetail.as_view(), name='location-detail'),
    path('calendar/geoloc/<str:GeoLoc>/', views.CalendarListByGeoLoc.as_view(), name='calendar-list-by-geoloc'),
]