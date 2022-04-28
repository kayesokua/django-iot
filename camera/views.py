from django.shortcuts import render, redirect
from django.http import HttpResponse,StreamingHttpResponse, HttpResponseServerError
from django.views.decorators import gzip
from camera.api.serializers import PiImageSerializer
from picamera.array import PiRGBArray
from picamera import PiCamera
from models import PiImage
from rest_framework.views import APIView
from rest_framework.response import Response
from camera.api import serializers

def setup(request):
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30
    rawCapture = PiRGBArray(camera, size=(640, 480))
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)

# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         ret,image = self.video.read()
#         ret,jpeg = cv2.imencode('.jpg',image)
#         return jpeg.tobytes()

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield(b'--frame\r\n'
#         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# def video_feed():
#     return HttpResponse(gen(camera()),mimetype='multipart/x-mixed-replace; boundary=frame')

# @gzip.gzip_page
# def setup(request): 
#     try:
#         return StreamingHttpResponse(gen(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")
#     except HttpResponseServerError as e:
#         print("aborted")

class PiImageAV(APIView):
    def get(self, request):
        gallery = PiImage.objects.all()
        serializer = serializers.PiImageSerializer(gallery, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.PiImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)