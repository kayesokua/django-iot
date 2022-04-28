from django.http import HttpResponse
from robot.extras.helper_functions import *
from robot.extras.gripper_motor import *
from robot.extras.wrist_motor import *

def setup(request):
    html = "<html><body>This describes the setup of the robotic arm</body></html>"
    return HttpResponse(html)

def gripper(request):
    gripper = motor_setup(13)
    to_full_open(gripper)
    grab(gripper)
    clean_up(gripper)
    html = "<html><body>This desribes the gripper</body></html>"
    return HttpResponse(html)

def wrist(request):
    wrist = motor_setup(11)
    homing(wrist)                        
    pour(wrist)
    homing(wrist)
    clean_up(wrist)
    html = "<html><body>This desribes the wrist</body></html>"
    return HttpResponse(html)

def upper_arm(request):
    html = "<html><body>This desribes the upper arm</body></html>"
    return HttpResponse(html)

def lower_arm(request):
    html = "<html><body>This desribes the lower arm./body></html>"
    return HttpResponse(html)

def waist(request):
    html = "<html><body>This is the waist. Start move</body></html>"
    return HttpResponse(html)

def test_gripper(request):
    html = "<html><body>This desribes the gripper</body></html>"
    return HttpResponse(html)

def test_wrist(request):
    html = "<html><body>Checking if the wrist arm is turning</body></html>"
    return HttpResponse(html)

def test_upper_arm(request):
    html = "<html><body>Checking if the upper arm is turning</body></html>"
    return HttpResponse(html)

def test_lower_arm(request):
    html = "<html><body>Checking if the lower arm is turning</body></html>"
    return HttpResponse(html)

def test_waist(request):
    html = "<html><body>Checking if the waist is turning</body></html>"
    return HttpResponse(html)