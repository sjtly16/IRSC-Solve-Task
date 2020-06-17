from django.urls import path
from .views import ScheduleAPI, ServerStateAPI

urlpatterns = [
    path('', ScheduleAPI.as_view(), name="schdule-task"),
    path('ping/', ServerStateAPI.as_view(), name="server-state"),

]
