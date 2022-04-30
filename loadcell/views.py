from django.http import HttpResponse
from django.shortcuts import render
from .utils import *
import time
import sys

def info(request):
    html = "<html><body>This explains the setup of the weigh sensor.</body></html>"
    return HttpResponse(html)

def clean_up():
    print("Cleaning GPIO channel")
    GPIO.cleanup()
    sys.exit()
    
def hx711_setup():
    GPIO.setwarnings(False)
    # Calculating the reference unit
    # If I got numbers around 32873 for an empty shot glass that weights 80g
    # Then reference unit is 32873 / 80 = 410.91
    referenceUnit = 32873/80
    hx = HX711(5, 6)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(referenceUnit)
    
def test(request):
    referenceUnit = 32873/80
    hx = HX711(5, 6)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(referenceUnit)
    hx711_setup()
    hx.reset()
    hx.tare()
    hx.tare_A()
    hx.tare_B()
    print("Let us begin weighing..")
    
    while True:
        val = hx.get_weight(5)
        res = "{:.2f}".format(val)
        print("Weigh sensor reads ",res, "g")
        hx.power_down()
        hx.power_up()
        time.sleep(1)
        result = res
        
        if int(val) > 60 and int(val) < 120:
            print("We recognise an empty shot glass!")
            print("Now its time to wait for the robot!")
            time.sleep(3)
            clean_up()
            return render("test.html", {"result":result, "success":"The robot recognises the drink is empty!"})
        else:
            return render("test.html", {"result":result})