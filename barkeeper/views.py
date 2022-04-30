import time
#from GPIOEmulator.EmulatorGUI import GPIO
#import RPi.GPIO as GPIO
from django.http import HttpResponse

def barkeeper_home(request):
    html = "<html><body>This shows the instructions of ordering and all it has served</body></html>"
    return HttpResponse(html)

def barkeeper_start(request):
    html = "<html><body>This starts the script</body></html>"
    return HttpResponse(html)

def barkeeper_reset(request):
    html = "<html><body>This stops the robot from all actions and homing</body></html>"
    return HttpResponse(html)

def barkeeper_task_validate(request):
    html = "<html><body>The expected action: validates that the barkeeper knows the drink and that the shot glass is empty</body></html>"
    return HttpResponse(html)

def barkeeper_task_grab(request):
    html = "<html><body>The expected action: grabbing the glass</body></html>"
    return HttpResponse(html)

def barkeeper_task_pour(request):
    html = "<html><body>The expected action: the gripper is turnning</body></html>"
    return HttpResponse(html)

def barkeeper_task_release(request):
    html = "<html><body>The expected action: releasing the drink</body></html>"
    return HttpResponse(html)

def events(request):
    html = "<html><body>This shows the number of times the barkeeper has responded</body></html>"
    return HttpResponse(html)
