

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
    path("plane-data/", views.PlaneListView.as_view(), name='planes'),
    path("plane-data/<str:pk>/", views.IndividualPlaneData.as_view(), name='plane details'),
    path("calendar/", views.CalendarListView.as_view(), name='calendars'),
    path("calendar/<date:pk>/", views.IndividualDateCalendar.as_view(), name='calendar date details'),
    path("plane-maintenance/", views.PlaneMaintenanceListView.as_view(), name='plane maintenance'),
    path("plane-maintenance/<str:pk>/", views.IndividualPlaneMaintenanceView.as_view(), name='plane maintenance details'),
    path("plane-maintenance/<str:pk>/", views.PlaneMaintenanceAircraftView.as_view(), name='plane maint. aircraft details'),
    path("part-maintenance/", views.PartMaintenanceListView.as_view(), name='part maintenance'),
    path("part-maintenance/<str:pk>/", views.IndividualPartMaintenanceView.as_view(), name='part maintenance details'),
    path("part-maintenance/<str:pk>/", views.PartMaintenanceAircraftView.as_view(), name='part maint. aircraft details'),
]