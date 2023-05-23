"""
URL configuration for ROUS_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from ROUS_API import views
from . import views

# router = routers.DefaultRouter()
# router.register('user', UserView, basename='userModel')
# router.register('base', BaseView, basename='baseModel')
# router.register('aircraft', AircraftView, basename='aircraftModel')
# router.register('catnum', CatNumView, basename='catNumModel')
# router.register('engCurrentTime', EngineCurrentTimeView, basename='engineTimeModel')

# urlpatterns = router.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path("user/", views.UserView.as_view(), name='users'),
    path("user/<int:id>/", views.UserInfo.as_view(), name='user details'),
    path("plane/", views.PlaneView.as_view(), name='planes'),
    path("plane/<int:id>/", views.PlaneInfo.as_view(), name='plane details'),
    path("maintenance/", views.MaintenanceView.as_view(), name='maintenance'),
    path("maintenance/<int:id>/", views.MaintenanceInfo.as_view(), name='maintenance details'),
    path("calender/", views.CalenderView.as_view(), name='calender'),
    path("calender/<int:id>/", views.CalenderInfo.as_view(), name='calender details'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
