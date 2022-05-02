from django.urls import path
from barkeeper.views import *
from barkeeper.api.viewsets import EventListAV, EventDetailAV

urlpatterns = [
    path('/', barkeeper_home, name='barkeeper_home'),
    path('/home', barkeeper_home, name='barkeeper_home'),
    path('/start', barkeeper_start, name='barkeeper_start'),
    path('/reset', barkeeper_reset, name='barkeeper_reset'),
    path('/task/validate', barkeeper_task_validate, name='barkeeper_task_validate'),
    path('/task/grab', barkeeper_task_grab, name='barkeeper_task_grab'),
    path('/task/pour', barkeeper_task_pour, name='barkeeper_task_pour'),
    path('/task/release', barkeeper_task_release, name='barkeeper_task_release'),
    path('/events', events, name='events'),
    path('api/', EventListAV.as_view(), name='api-event-list'),
    path('api/<int:pk>', EventDetailAV.as_view(), name='api-event-detail'),
]