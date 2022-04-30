from picamera import PiCamera
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import pytesseract
from time import sleep
from camera.api import serializers
from camera.api.serializers import PiImageSerializer
from .models import PiImage
from .forms import PiImageForm
import glob

import cv2

def camera_setup():
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30
    rawCapture = PiRGBArray(camera, size=(640, 480))

stills = glob.glob('/rapstill/*.jpg')
still_count = len(stills)

def camera_live(request):
    camera_setup()
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
         image = frame.array
         cv2.imshow("Frame", image)
         key = cv2.waitKey(1) & 0xFF
         rawCapture.truncate(0)
         return render(request, 'index.html', {'form':PiImageForm()})

def capture(request):
    global still_count
    print ("Saving Still...")
    still_count +=1
    camera.capture('/rapstill/' + str(still_count) + '.jpg')
    camera.stop_preview()
    return redirect('camera_live')
        
def capture_detail(request,pk):
    html = "<html><body>Just displays the image here</body></html>"
    return HttpResponse(html)

    # img_preview = get_object_or_404(PiImage, pk=pk)
    # if request.method == 'GET':
    #     form = PiImageForm(instance=img_preview)
    #     return render(request, 'preview.html', {'img_preview':img_preview, 'form':form})
    # else:
    #     try:
    #         form = PiImageForm(request.POST, request.FILES, instance=img_preview)
    #         form.save()
    #         return redirect('currenttodos')
    #     except ValueError:
    #         return render(request, 'preview.html', {'img_preview':img_preview, 'form':form})

# from django.core.files import File
# from django.core.files.base import ContentFile
# from django.core.files.temp import NamedTemporaryFile

# def capture_upload(request):
#     context = dict()
#     if request.method == 'POST':
#         image_path = request.POST["src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
#         image = NamedTemporaryFile()
#         image.write(urlopen(path).read())
#         image.flush()
#         image = File(image)
#         name = str(image.name).split('\\')[-1]
#         name += '.jpg'  # store image in jpeg format
#         image.name = name
#         if image is not None:
#             obj = PiImage.objects.create(username=username, image=image)  # create a object of Image type defined in your model
#             obj.save()
#             context["path"] = obj.image.url  #url to image stored in my server/local device
#             context["username"] = obj.username
#         else :
#             return redirect('/')
#         return redirect('any_url')
#     return render(request, 'index.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.         
