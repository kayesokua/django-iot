from django.urls import path
from robot.views import setup,gripper
from robot.views import *

urlpatterns = [
    path('/', robot_homing, name='robot_homing'),
    path('/reset', robot_homing, name='robot_homing'),
    path('/gripper', test_gripper_range, name='test_gripper_range'),
    path('/wrist', test_wrist_range, name='test_wrist_range'),
    path('/upper_arm', test_upper_arm_range, name='test_upper_arm_range'),
    path('/lower_arm', test_lower_arm_range, name='test_lower_arm_range'),
    path('/waist', test_waist_range, name='test_waist_range')
]