from django.http import HttpResponse
from loadcell.extras.hx711 import HX711
import time

def setup(request):
    html = "<html><body>This describes the setup of the weighing sensor</body></html>"
    return HttpResponse(html)

def weigh_test(request):
    referenceUnit = 1
    hx = HX711(5, 6)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(referenceUnit)
    hx.reset()
    hx.tare()
    print("Tare done! Add weight now...")
    
    while True:
        val = hx.get_weight(5)
        print(val)
        hx.power_down()
        hx.power_up()
        time.sleep(0.1)
        html = "<html><body>It is now %s g</body></html>" % val
        return HttpResponse(html)