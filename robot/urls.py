from django.urls import path
from robot.views import setup,gripper
from robot.views import *

urlpatterns = [
    path('/', setup, name='setup'),
    path('/gripper', gripper, name='gripper'),
    path('/gripper/test', test_gripper, name='test_gripper'),
    path('/wrist', wrist, name='wrist'),
    path('/wrist/test', test_wrist, name='test_wrist'),
    path('/upper_arm', upper_arm, name='upper_arm'),
    path('/upper_arm/test', test_upper_arm, name='test_upper_arm'),
    path('/lower_arm', lower_arm, name='lower_arm'),
    path('/lower_arm/test', test_lower_arm, name='test_lower_arm'),
    path('/waist', waist, name='waist'),
    path('/waist/test', test_waist, name='test_waist')
]