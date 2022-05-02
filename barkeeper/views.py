import time
#from GPIOEmulator.EmulatorGUI import GPIO
#import RPi.GPIO as GPIO
from django.http import HttpResponse

def barkeeper_home(request):
    #create about me page
    html = "<html><body>This shows the instructions of ordering and all it has served</body></html>"
    return HttpResponse(html)

def barkeeper_start(request):
    #redirect to camera
    html = "<html><body>This starts the script</body></html>"
    return HttpResponse(html)

def barkeeper_reset(request):
    #redirect to homing
    html = "<html><body>This stops the robot from all actions and homing</body></html>"
    return HttpResponse(html)

def barkeeper_task_validate(request):
    #redirect to loadcell
    html = "<html><body>The expected action: validates that the barkeeper knows the drink and that the shot glass is empty</body></html>"
    return HttpResponse(html)

def barkeeper_task_grab(request):
    #moves to location of the bottle
    html = "<html><body>The expected action: grabbing the glass</body></html>"
    return HttpResponse(html)

def barkeeper_task_pour(request):
    #pours it back to the shot glass that is on the load cell
    html = "<html><body>The expected action: the gripper is turnning</body></html>"
    return HttpResponse(html)

def barkeeper_task_release(request):
    #open the gripper
    html = "<html><body>The expected action: releasing the drink</body></html>"
    return HttpResponse(html)

def events(request):
    #just displaying all the events of the robot
    html = "<html><body>This shows the number of times the barkeeper has responded</body></html>"
    return HttpResponse(html)
