import RPi.GPIO as GPIO
import time
from django.http import HttpResponse
GPIO.setmode(GPIO.BOARD)

#Helper Functions:
def motor_setup(pin):
    GPIO.setup(pin, GPIO.OUT)
    motor = GPIO.PWM(pin, 50)
    motor.start(0)
    return motor
    
def degree_to_DC(degree):
    dc = 1/18*(degree)+2
    return dc

def change_DC(motor,dc):
    motor.ChangeDutyCycle(dc)
    time.sleep(0.2)
    motor.ChangeDutyCycle(0)
    time.sleep(0.8)

def clean_up(motor):
    motor.stop()
    GPIO.cleanup()

#Gripper Functions
def to_full_open(motor):
    pos = 60
    dc = degree_to_DC(pos)   
#     print(dc)
#     print(motor)
    change_DC(motor, dc)
    time.sleep(0.2)

def grab(motor):
#     for pos in range(50,-1,-1):
#         dc = degree_to_DC(pos)
#         change_DC(motor, dc)
#         print("current position: ",pos)
#         time.sleep(0.05)
    dc = degree_to_DC(0)
    change_DC(motor, dc)

#Wrist Motor Functions
def pour(motor) :
    pos = 80
    dc = degree_to_DC(pos)
    change_DC(motor,dc)
    
def homing(motor):
    pos = 180
    dc = degree_to_DC(pos)
    change_DC(motor,dc)

#Set up
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