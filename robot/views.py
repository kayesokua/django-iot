import time
from django.http import HttpResponse
from .utils import *

Pins = {
   13: {"name" : "gripper", "homing_pos": 60, "sleep_time":0.2,"task_pos":0, "sleep_time_task":0.05},
   11: {"name" : "wrist", "homing_pos": 0, "sleep_time":0.0,"task_pos":80, "sleep_time_task":0.0},
   15: {"name" : "upper_arm", "homing_pos": 150, "sleep_time":0.0,"task_pos":120, "sleep_time_task":0.0},
   37: {"name" : "lower_arm", "homing_pos": 120, "sleep_time":0.0,"task_pos":0, "sleep_time_task":0.0},
   35: {"name" : "waist", "homing_pos": 0, "sleep_time":0.0,"task_pos":0, "sleep_time_task":0.0}
   }

def robot_homing(request):
    for pin,config in Pins.items():
        GPIO.setmode(GPIO.BOARD)
        motor = motor_setup(pin)
        homing_pos = config["homing_pos"]
        dc = degree_to_DC(homing_pos)
        change_DC(motor,dc)
        time.sleep(config["sleep_time"])
        clean_up(motor)
    html = "<html><body>This should let you view the robot that is running</body></html>"
    return HttpResponse(html)

def test_gripper_range(request):
    GPIO.setmode(GPIO.BOARD)
    gripper = motor_setup(13)
    test_range(gripper)
    clean_up(gripper)
    html = "<html><body>This lets you test the gripper</body></html>"
    return HttpResponse(html)

def test_wrist_range(request):
    GPIO.setmode(GPIO.BOARD)
    wrist = motor_setup(11)
    test_range(wrist)
    clean_up(wrist)
    html = "<html><body>This lets you test the wrist</body></html>"
    return HttpResponse(html)

def test_upper_arm_range(request):
    GPIO.setmode(GPIO.BOARD)
    upper_arm = motor_setup(15)
    test_range(upper_arm)
    clean_up(upper_arm)
    html = "<html><body>Checking if the upper arm is turning</body></html>"
    return HttpResponse(html)

def test_lower_arm_range(request):
    GPIO.setmode(GPIO.BOARD)
    lower_arm = motor_setup(37)
    test_range(lower_arm)
    clean_up(lower_arm)
    html = "<html><body>Checking if the lower arm is turning</body></html>"
    return HttpResponse(html)

def test_waist_range(request):
    GPIO.setmode(GPIO.BOARD)
    waist = motor_setup(35)
    test_range(waist)
    clean_up(waist)
    html = "<html><body>Checking if the waist is turning</body></html>"
    return HttpResponse(html)