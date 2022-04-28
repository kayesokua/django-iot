from django.urls import path
from barkeeper.views import *

urlpatterns = [
    path('/', barkeeper_home, name='barkeeper_home'),
    path('/home', barkeeper_home, name='barkeeper_home'),
    path('/start', barkeeper_start, name='barkeeper_start'),
    path('/reset', barkeeper_reset, name='barkeeper_reset'),
    path('/task/validate', barkeeper_task_validate, name='barkeeper_task_validate'),
    path('/task/grab', barkeeper_task_grab, name='barkeeper_task_grab'),
    path('/task/pour', barkeeper_task_pour, name='barkeeper_task_pour'),
    path('/task/release', barkeeper_task_release, name='barkeeper_task_release'),
    path('/events', events, name='events')
]