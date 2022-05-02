import datetime
from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep
import requests
from PIL import Image
from numpy import asarray
import pytesseract

camera_switch = True
now = datetime.datetime.now()
filedate = str(now.strftime('%Y%m%d%H%M%S'))

camera = PiCamera()
camera.framerate = 30
camera.preview_fullscreen=False
camera.preview_window=(640, 480, 640, 480)
camera.resolution = (640, 480)
camera.start_preview()
sleep(10)
camera.stop_preview()
camera_switch = False

#To save internal storage space, only one image is saved and it is being converted to np arrays

camera.capture('/home/pi/Desktop/image.jpg')
print(filedate+' is now saved.')

if camera_switch is False:
    image = Image.open('/home/pi/Desktop/image.jpg')
    image_ocr = pytesseract.image_to_string(image, timeout=2)
    image_npdata = asarray(image)
    print(image_ocr)
    print(image_npdata)
